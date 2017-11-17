def inputInfo(s):
    p=dict()

    print('输入名字和年龄信息')
    flag0=1

    while flag0==1:
        n=input("name:")
        age=int(input("age:"))
        
            
        p["name"]=n
        p["age"]=age
        s.append(n)
        s.append(age)
        print('按回车继续,输入其他值则停止')
        m=input()
        if m!='':
            flag0=0
        
        #输入信息 输入为空时候停止
    print('输入完毕')

def shuchu():
    flag1=int(input("按1输出已储存信息"))
    if flag1==1:
        for i in range (0,len(stu),2):
            
            print('name=%s  age=%d'%(stu[i],stu[i+1]))   


stu=[]
inputInfo(stu)
shuchu()
