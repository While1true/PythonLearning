#encoding:utf_8
print('你好')

def fun(a,b):
    return a+b

print(fun(1,3))

def funfun(f,a):
    return f(a,a*a)

print(funfun(fun,9))