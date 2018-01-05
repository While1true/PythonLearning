#encoding:utf_8
#int range()数据大的时候会卡死
import time as test
import sys
import method as te
# dic={'a':'aa','b':1}
# print(dic),type(dic)
zz = test.clock()
print(str(te.funfun(te.fun,2)))
def fun(total):
    zz = test.clock()
    print('----------------'),zz-test.clock()
    l=[]
    i=0
    while (i < total):
        l.append(i)
        time = test.clock() - zz
        if(i==0):
           print(time)
        i = i + 1
        try:
           test.sleep(0.01)
        except Exception as a:
            print(a.message)
        if(time>5):
            print('时间太久了')
            break
    return l
zz=test.clock()
# lst=[(x,x) for x in xrange(2000000)]
lst=fun(sys.maxint)
print str(test.clock()-zz)
# zz=test.clock()
# dic=dict(lst)
# print('======================================')
# print str(test.clock()-zz)
# zz=test.clock()
# for keya,a in dic.iteritems():
#     doc=keya+a
#
# print('======================================')
# print str(test.clock()-zz)