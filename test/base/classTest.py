#encoding:utf_8
class Animal(object):
    age = 0
    name = None

    def __init__(self):
       print('在干啥啊啊啊 啊')

    def say(self,words):
        print self.name,(words)

    def setName(self,name):
        self.name=name

man= Animal()
print(man.name)

man.say("dddd")

man.setName("nsdss")
print(man.name)
zz=Animal()
print(zz.name)
zz.setName('dsds')
Animal.name='ddd'
print(man.name)
print(zz.name)

cc=Animal()
print(cc.name)

class zz(Animal):
    name = "aa"

zz.name='sss'
cc=zz()
print(cc.name)