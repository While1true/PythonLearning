#encoding:utf_8
import os
f=open(u'C:\\Users\\乐城\\Desktop\\新建文本文档.txt','r')

f2=open(u'C:\\Users\\乐城\\Desktop\\来自py的试炼\来自py的试炼.txt','r+')
for l in f:
    print(l.replace("\n","").decode('gbk'))
pathz=u'C:\\Users\\乐城\\Desktop'

def dd(fs,path):
    for s in fs:
        zz=os.path.join(path,s)
        if(os.path.isfile(zz) or os.path.islink(zz)):
            f2.writelines(os.path.join(path,s).encode("gbk")+"\r\n")
            print(os.path.join(path,s))
        elif(os.path.isdir(zz)):
            print(zz.encode('gbk')+"--------------"+"\r\n")
            f2.writelines(zz.encode('gbk')+"--------------"+"\r\n")
            dd(os.listdir(zz),zz)
        else:
            f2.writelines('\nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'+zz.encode('gbk')+"\r\n")
            print 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
            print(zz)
dd(os.listdir(pathz),pathz)
f2.flush()
f2.close()
f.close()