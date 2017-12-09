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
        os.chdir(mkpath)
        f.close()
        
        
    except:
        print("error")    



url2='http://www.idanbooru.com/posts/{}'#format函数改pn={}  用循环实现

makepath(mkpath)
i=2879142
j=2879144
#flag=0
def getpicture(i,j):
    for i in range(i,j):
        bdText=getHtmlText(url2.format(i))

        #print(bdText)



        bs=BeautifulSoup(bdText,'html.parser')

        result=bs.select('#image')
        try:
            r=result[0]


            #print(r)
            #number_url = re.findall('<img src="/images/(.)\.gif"/>', konachan.text, re.S)

            src=r.attrs['src']
            #print(src)
            ext='http://www.idanbooru.com'+src
            #print(ext)
            hz=re.findall(re.compile('.+\.(.+)'),ext)
            img=getHtmlBin(ext)
            file='{}.{}'.format(i,hz[0])
            print(file)

            savePic(img,file)
        except:
            print('该图片不存在')        
getpicture(i,j)
#try:
   # getpicture(i,j)
    #flag=i+1  
                
#except:
 #   flag=flag+1
  #  return print('该图片不存在')
#finally: getpicture(flag+2,j)

    
'''
http://a.hiphotos.baidu.com/image/pic/item/3812b31bb051f819766026d6d1b44aed2f73e7e1.jpg
'''
    
#正则表达式寻找文件格式 jpg或者png等等   进行相应的替换
