#encoding:utf_8
s=['1','2','3','dd','HJ你的',"    ","1"]
str='----'
result=str.join(s)
print(result)
a='z'
a=result.ljust(20,'0')
print a
print(result.rjust(len(result)+50,'z'))
print(result.center(len(result)+50,'z'))