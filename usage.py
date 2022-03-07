import sys,os
sys.path.append(os.getcwd())

from LegadoParser2.Search import search
from LegadoParser2.BookInfo import getBookInfo
from LegadoParser2.ChapterList import getChapterList
from LegadoParser2.Chapter import getChapterContent
import json
from pprint import pprint

from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
from yoshu_spider import *
import time,threading


def main():

    with open('booksource.txt', 'r', encoding='utf-8') as f:
        bookSource = json.loads(f.read())
    print('-' * 20 + '开始搜索' + '-' * 20)
    searchResult = search(bookSource, '我的')
    if searchResult:
        pprint(searchResult[0])
        print('-' * 20 + '开始获取详情' + '-' * 20)
        bookInfo = getBookInfo(bookSource, searchResult[0]['bookUrl'])
    else:
        bookInfo = {}
    if bookInfo:
        pprint(bookInfo)
        print('-' * 20 + '开始获取章节列表' + '-' * 20)
        chapterList = getChapterList(bookSource, bookInfo['tocUrl'])
        print(f'列表大小{len(chapterList)}')
    else:
        chapterList = []
    if chapterList and len(chapterList) > 2:

        pprint(chapterList[:3])
        print('-' * 20 + '开始获取内容' + '-' * 20)
        bookContent = getChapterContent(
            bookSource, chapterList[0]['url'], chapterList[1]['url'])
    elif chapterList:
        pprint(chapterList)
        print('-' * 20 + '开始获取内容' + '-' * 20)
        bookContent = getChapterContent(
            bookSource, chapterList[0]['url'], chapterList[1]['url'])
    else:
        print('-' * 20 + '开始获取内容' + '-' * 20)
        bookContent = {}
    if bookContent:
        pprint(bookContent)
    print('-' * 20 + '结束' + '-' * 20)

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
        bS_index+=1
        if src["using"]:
            continue

        hit={}
        try:
            result=search(src,key)
            # print("search in:"+src["bookSourceName"])
        except:
            # print("errSearch in "+src["bookSourceName"])
            continue
        if result:
            for r in result:
                if r["name"]==key:
                    hit=r
                    src["using"]=True
                    print("finded:",r)
                    break
        
        if not hit:
            continue

        try:
            result=getBookInfo(src,hit["bookUrl"])
            chapterList=getChapterList(src,result['tocUrl'])
        except Exception as e:
            print(e)
            continue


        if chapterList: 
            books[key].isDownload(True) 
            for chapter in range(startChapter,len(chapterList)):
                try:
                    content=getChapterContent(src,chapterList[chapter]["url"])
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
    # get("疯巫妖的实验日志")
    pool=ThreadPoolExecutor(max_workers=16)
    all_task=[pool.submit(get,(key)) for key in names]
    wait(all_task,return_when=ALL_COMPLETED)