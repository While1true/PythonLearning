#encoding:gbk
print("i am %r,my best job is %s" % ('Mao','玩')).decode('gbk')
print("i am %(name)s,my best job is %(job)s" % {'name':'Mao','job':'玩'}).decode('gbk')

print("i am %(name)e,my best job is %(job)E" % {'name':5,'job':6}).decode('gbk')
print("i am %(name)f,my best job is %(job)F" % {'name':1.1,'job':2}).decode('gbk')

print("%10x" % 100000)
print("%.6f" % 100000)
print("% 4d" % 5)
print("%6.3f" % 2.3)
print("%.*f" % (2, 14))