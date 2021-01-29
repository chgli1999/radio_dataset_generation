#修改文件名
#coding=gbk
import os
import sys


path = os.getcwd()
#filename = 'ImageSet'
filename = 'Annotations'
filepath = os.path.join(path,filename)
filelist = os.listdir(filepath)
for i in range(len(filelist)):
    name = filelist[i]
    Olddir=os.path.join(filepath,name)
    name = name.replace('Jan','1')  #改变字符串中指定的字符
    name = name[:16]+name[19:]  #字符串切片
    Newdir=os.path.join(filepath,name)
    os.rename(Olddir,Newdir)   #修改文件名