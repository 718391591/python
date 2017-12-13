import requests
import re
from bs4 import BeautifulSoup
import os

    
mkpath='d:\\picture'   
def makepath(path):
    path=path.strip()
    path=path.rstrip('\\') #去除空格和\\
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs (path)
        print(path+'创建成功')
        
    else:
        print(path+'目录已存在')
        
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



url2='http://www.idanbooru.com/posts/{}'#format函数改pn={}  用循环实现

makepath(mkpath)
print(os.getcwd())
os.chdir(mkpath)
print(os.getcwd())
i=int(input('起点编号'))
j=int(input('终点编号'))
#flag=0
'''def getbigpicture(i,j):
    for i in range(i,j):
        bdText=getHtmlText(url2.format(i))
        bs=BeautifulSoup(bdText,'html.parser')
        result=bs.select('#image-resize-link')
        r=result[0]
        src=r.attrs['href']
        print(src)
        ext='http://www.idanbooru.com'+src
        print(ext)
        hz=re.findall(re.compile('.+\.(.+)'),ext)
        img=getHtmlBin(ext)

        file='{}.{}'.format(i,hz[0])
        print(file)

        savePic(img,file)
        '''
def getpicture(i,j):
    for i in range(i,j):
        bdText=getHtmlText(url2.format(i))
        bs=BeautifulSoup(bdText,'html.parser')
        try:
            result=bs.select('#image-resize-link')
            r=result[0]
            src=r.attrs['href']
            print(src)
            ext='http://www.idanbooru.com'+src
            print(ext)
            hz=re.findall(re.compile('.+\.(.+)'),ext)
            img=getHtmlBin(ext)
            file='{}.{}'.format(i,hz[0])
            print(file)
            savePic(img,file) 

        except:
            try:
                
                result=bs.select('#image')
                r=result[0]
                print(r)
                src=r.attrs['src']
                print(src)
                ext='http://www.idanbooru.com'+src
                hz=re.findall(re.compile('.+\.(.+)'),ext)
                img=getHtmlBin(ext)
                file='{}.{}'.format(i,hz[0])
                print(file)
                savePic(img,file)
            except :
                print('又出错了,这次是作者要求网站把图删除了')
getpicture(i,j)



    
#正则表达式寻找文件格式 jpg或者png等等   进行相应的替换
