import requests
import re
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return ""

def getHtmlBin(url):
    try:
        r=requests.get(url)
        r.raise_for_status()        
        return r.content
    except:
        return []

def savePic(img,filename):
    try:
        f=open(filename,'wb')
        f.write(img)
        f.close()
    except:
        print("error")    


url2='http://image.baidu.com/search/wisemiddetail?tn=wisemiddetail&ie=utf8&word={}&fmpage=detail&pn={}&gsm=d&size=&pos=next'#format函数改pn={}  用循环实现
num=3
types=['汽车','风景','壁纸']
for j in types:
    for i in range(num):
        bdText=getHtmlText(url2.format(j,i))

        #print(bdText)
        #body > div:nth-child(8) > a
        #/html/body/div[5]/a

        bs=BeautifulSoup(bdText,'html.parser')
        result=bs.select('body > div:nth-of-type(5) > a')
        #print(result)
        r=result[0]
        print(r)
        src=r.attrs['href']
        print(src)
        ext=re.findall(re.compile('.+\.(.+)'),src)
        
        img=getHtmlBin(src)
        file='{}.{}.{}'.format(j,i,ext[0])
        print(file)
        savePic(img,file)
'''
http://a.hiphotos.baidu.com/image/pic/item/3812b31bb051f819766026d6d1b44aed2f73e7e1.jpg
'''
    
#正则表达式寻找文件格式 jpg或者png等等   进行相应的替换
