import sys,os
sys.path.append(os.getcwd())

from LegadoParser2.Search import search
from LegadoParser2.BookInfo import getBookInfo
from LegadoParser2.ChapterList import getChapterList
from LegadoParser2.Chapter import getChapterContent
from LegadoParser2.RulePacket import compileBookSource
import json
from pprint import pprint

from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
from yoshu_spider import *
import time,threading


books={}
names=[]
bookSource={}

def init():
    h=pickle_Helper("temp/Books.pickle")
    global books,names,bookSource
    books=h.load()
    names=list(books.keys())
    with open('bookSource/bookSource.json', 'r', encoding='utf-8') as f:
        bookSource = json.loads(f.read())
    for src in bookSource:
        src["using"]=False

def get(key,startChapter=0):
    bS_index=0
    
    for src in bookSource:

        src=compileBookSource(src)

        bS_index+=1
        if src["using"]:
            continue

        hit={}
        try:
            result=search(src,key)
            print("search in:"+src["bookSourceName"])
        except:
            print("errSearch in "+src["bookSourceName"])
            continue
        if result:
            for r in result:
                if r["name"]==key:
                    lock=threading.Lock()
                    lock.acquire()
                    hit=r
                    src["using"]=True
                    print("finded:",r)
                    lock.release()
                    break
        
        if not hit:
            continue

        try:
            result=getBookInfo(src,hit["bookUrl"],hit["variables"])
            chapterList=getChapterList(src,result['tocUrl'],result["variables"])
        except Exception as e:
            print(e)
            continue


        if chapterList: 
            books[key].isDownload(True) 
            for chapter in range(startChapter,len(chapterList)):
                try:
                    content=getChapterContent(src,chapterList[chapter]["url"],chapterList[chapter]["variables"])
                    print("try to get ",str(chapterList[chapter]))
                except Exception as e:
                    print("getErr:",chapter,bS_index,e)
                    continue
                if content:
                    with open("books/"+key+".txt","a") as f:
                        f.write(chapterList[chapter]["name"]+"\n")
                        f.write(content["content"].strip()+"\n\n")
                    time.sleep(1.5)
        
        if books[key].Down:
            break
        
        
            

        
        

if __name__ == '__main__':
    init()
    get("疯巫妖的实验日志")
    # pool=ThreadPoolExecutor(max_workers=32)
    # all_task=[pool.submit(get,(key)) for key in names]
    # wait(all_task,return_when=ALL_COMPLETED)