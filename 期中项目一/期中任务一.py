#!/usr/bin/env python
# coding: utf-8

# In[84]:


import os
import re
os.chdir('C:\\Users\\Administrator.CHAO-20180828JC\\book')

def SplitEC(article,name):  #分离中英文
    zech=re.compile(r'[\u4e00-\u9fa5,、,，,“,”,。,0-9,？,——,《,》,：]')
    zeen=re.compile(r'[\u0061-\u007a,\u0041-\u005a,\u0020,．,，,",0-9,\',？,！]')
    en="".join(zeen.findall(article))
    ch="".join(zech.findall(article))
    
    os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\en')
    wen=open(name+'en.txt','w')
    en1=en.replace("\n"," ")
    #en2=en1.replace("．",".\n")
    enx=re.sub(r'[，！ —？0-9'']{2,}',' ',en1)
    eny=enx.replace("，",", ")
    enz=eny.replace("．",". ")
    ens=enz.replace("？",'? ')
    en2=ens.replace("！ ","! ")
    #en2=ena.replace("","")
    wen.write(en2)
    wen.close()  #写入英文文件夹
    
    os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\zh')
    wch=open(name+'zh.txt','w')
    ch1=ch.replace("。","。\n")
    ch2=re.sub(r'[，—？0-9]{2,}',' ',ch1)
    wch.write(ch2)
    wch.close()  #写入中文文件夹
    
    #返回文件原路径
    os.chdir(r'C:\\Users\\Administrator.CHAO-20180828JC\\book')
    
for i in os.listdir():  #遍历当前文件夹里的文件名
    name=i[:-4]  #只取名字前面部分，不要.txt
    ar=open(i,'r')
    article=ar.read()
    ar.close()
    SplitEC(article,name)


# In[85]:


import os
import re
import jieba
import jieba.analyse
import csv


list1=os.listdir(r'C:\Users\Administrator.CHAO-20180828JC\output\zh')  #遍历当前文件夹里的文件名



#中文词频

for lis in list1: 
    os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\zh')
    article=open(lis,'r')
    str1=article.read()
    
    dele = {'。','！','？','的','“','”','（','）',' ','》','《','，',' ','1'}  #删去部分停用词
    article.close()
    words=list(jieba.cut(str1))
    word={}
    xrset=set(words)-dele  #减去标点符号和‘的’。                           
    #print(xrset)
    for w in xrset:
        if len(w)>1:
            word[w]=words.count(w)
    wordslist=sorted(word.items(),key=lambda x:x[1],reverse=True)
    
    os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\zh_freq')
    #csv1 = '1A_{}.csv'.format(str(i+1)+"."+name[i])
    csv1=lis[:-4]+'.csv'
    headers = ['words','freq']
    with open(csv1, 'w') as f:  #写入内容
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        #for i in wordslist:
        f_csv.writerows(wordslist)
    f.close()


# In[92]:


#英文词频
os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\en')
list1=os.listdir()  #遍历当前文件夹里的文件名
#print(list1)
for lis in list1: 
    os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\en')
    article=open(lis,'r')
    str2=article.read()
    #print(str1)
    str1=str1.split()
    enword={}
    for w in str1:
        if len(w)>1:
            enword[w]=str1.count(w)
    wordslist=sorted(enword.items(),key=lambda x:x[1],reverse=True)
    print(enword)
    7h
    os.chdir(r'C:\Users\Administrator.CHAO-20180828JC\output\en_freq')
    #csv1 = '1A_{}.csv'.format(str(i+1)+"."+name[i])
    csv1=lis[:-4]+'.csv'
    headers = ['words','freq']
    with open(csv1, 'w') as f:  #写入内容
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        #for i in wordslist:
        f_csv.writerows(wordslist)
    f.close()


# In[ ]:




