#encoding_utf_8

import re
#1-1
rex='[bh][aiu]t'

str='batbitbuthathithut'

groups=re.findall(rex,str)
print(groups)

#1-2
name='var    maoi'
rex=r'\s+'
result=re.split(rex,name)
print(result)

#1-3
rex=r'''(?x),|[ ]'''
name='wgat,what 122'
result=re.split(rex,name)
print(result)


#1-5
res=r'\d+\s(?:\w+\s)*\w+'
address='3120 De la Cruz Bizopjj'
address2='212 Bizopjj'
groups=re.search(res,address).group()
print(groups)

groups=re.search(res,address2).group()
print(groups)

#1-6
ends=['.edu','.net','.com','.cn']
start=['www.','http://','https://']
rex='(?:^www\.|http://|http://)(?:\w+\.)+(?:edu|net|com|cn)$'
net1='www.hao123.com'
net2='www.hao123.zzz.cn'
net3='www.zz.hao123.net'
net4='www.hao123.edu'
net5='http://www.hao123.edu'
net6='http://www.hao123.qq.bb.ws.edu'
print(re.match(rex,net1).group())
print(re.match(rex,net2).group())
print(re.match(rex,net3).group())
print(re.match(rex,net4).group())
print(re.match(rex,net5).group())
print(re.match(rex,net6).group())

#1-9
f=.330001
rex='\d*\.\d+'
ss=re.match(rex,f.__str__()).group()
print(ss)

rex=r"(?x)<type[ ]'(?P<type>\w+)'>"
def fun(types):
    return re.match(rex,types).group("type")
print(fun("<type 'float'>"))