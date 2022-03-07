import requests,os
from bs4 import BeautifulSoup as bs
import re,time
import pickle

url='https://www.yousuu.com/bookstore/?channel=0&classId&tag&countWord&status&update=2&sort&page=%d'


headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'Hm_lvt_42e120beff2c918501a12c0d39a4e067=1644460042,1644460428; Hm_lpvt_42e120beff2c918501a12c0d39a4e067=1644460428',
'Host': 'www.yousuu.com',
'If-None-Match': '"e515-FLCcwuavfWN033dExBuWmyzl9Hw"',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}



class pickle_Helper:
    def __init__(self,f):
        self.file=f

    def save(self,o):
        with open(self.file,'wb') as f:
            pickle.dump(o,f)

    def load(self):
        with open(self.file,'rb') as f:
            return pickle.load(f)

class Book:
    def __init__(self,name,score,score_Ps,last_updata,page):
        self.bName=name
        self.bScore=score
        self.bPerson=score_Ps
        self.bLastUp=last_updata
        self.bPage=page
        self.Down=False

    def isDownload(self,v):
        self.Down=v


Book_map={'C_page': 1}
PAGE_SAVE=True
DEBUG=False

def catch(i):
    h_save="temp/page_save%d"%i
    pkl=pickle_Helper(h_save)

    if(os.path.exists(h_save)):
        html=pkl.load()
        print("loaded!")
    else:
        html=requests.get(url%i,headers=headers)

    if(DEBUG):
        with open("temp/debug.html","w") as f:
            f.write(html.text)
    
    if(PAGE_SAVE):
        pkl.save(html)

    soup_1=bs(html.text,"html.parser")

    names=[i.text for i in soup_1.select("a.book-name")]
    pages=[i["href"] for i in soup_1.select("a.book-name")]
    tag_scores=soup_1.select("p.hidden-md-and-up")
    for i in range(len(tag_scores)):
        if(not len(tag_scores[i].text.strip().split('：'))==2):
            tag_scores[i].string="0：0(0人)"
    # print(tag_scores)
    scores=[float(i.text.strip().split('：')[1].split("(")[0]) for i in tag_scores]
    scores_persons=[int(i.text.strip().split('：')[1].split("(")[1].replace("人)","")) for i in tag_scores]
    lUpdatas=[i.text for i in soup_1.select("span.el-tooltip")]


    global Book_map
    for j in range(len(names)):
        print(names[j])
        Book_map[names[j]]=Book(names[j],scores[j],scores_persons[j],lUpdatas[j],pages[j])
    
    Book_map['C_page']=i

    print("current length:"+str(len(Book_map)-1)+"\n")

    

    # print(names)

def run():
    if(not os.path.exists("temp")):
        os.mkdir("temp")
    global Book_map
    Bm_save="temp/Books.pickle"
    pkl=pickle_Helper(Bm_save)
    if(os.path.exists(Bm_save)):
        Book_map=pkl.load()
    for i in range(Book_map["C_page"],500):
        # if(Book_map["C_page"]>=3):
        #     break
        catch(i)
        time.sleep(3)
        pkl.save(Book_map)

    
    
def getP():
    global Book_map
    Bm_save="temp/Books.pickle"
    pkl=pickle_Helper(Bm_save)
    if(os.path.exists(Bm_save)):
        Book_map=pkl.load()
    else:
        print("file not exists.")
    # del Book_map['C_page']
    # for key,value in Book_map.items():
    #     print(key+"\t%f\t%d\t%s"%(value.bScore,value.bPerson,value.bLastUp))
    # print(value)

def debug():
    catch(143)

if __name__=="__main__":
    run()
