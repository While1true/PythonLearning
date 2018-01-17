# encoding:utf_8
import urllib
import urllib2

import bs4
from bs4 import BeautifulSoup
import re
import time
import sys
import  json
import threading

import  os
list=[]
os_open = open('11.html','rb')
reads = os_open.read()
print(reads)
soup = BeautifulSoup(reads, 'lxml')

a=soup.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like')
list.extend(a)

os_open = open('12.html','rb')
reads = os_open.read()
print(reads)
soup = BeautifulSoup(reads, 'lxml')
a=soup.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like')
list.extend(a)

os_open = open('16.html','rb')
reads = os_open.read()
print(reads)
soup = BeautifulSoup(reads, 'lxml')
a=soup.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like')
list.extend(a)

print(list.__len__())
from Sql import Mydb
from generater import getType
dbhandler=Mydb()
for eachmessage in list:
    if (type(eachmessage) is not bs4.element.Tag):
        continue
    message = {'come': '纻麻兰若诗词'}
    try:
        namez = eachmessage.find(class_='WB_info').a.text
        # if(namez not in fromz):
        #     continue
        message['fid'] = eachmessage['tbinfo'].split('=')[1]
        message['mid'] = eachmessage['mid']

        timeinfo = eachmessage.find(class_='WB_from S_txt2').find(name='a')
        message['timestr'] = timeinfo['title']
        message['datelong'] = timeinfo['date']

        contentinfo = eachmessage.find(class_='WB_text W_f14')
        message['content'] = contentinfo.contents[0].strip().decode('utf8')
        try:
            if contentinfo.a:
                for hrefStr in contentinfo.a.contents:
                    if (type(hrefStr) is bs4.element.NavigableString):
                        message['hrefStr'] = getType(hrefStr.strip())
                        break
                message['href'] = contentinfo.a['href'].decode('utf8')

            message['category'] = '纻麻兰若诗词'
            imgsbox = eachmessage.find(class_='media_box')
            if (imgsbox):
                imgs = imgsbox.find_all(name='img')
                imgss = []
                if (imgs):
                    for img in imgs:
                        if (img['src']):
                            imgss.append(img['src'])
                if (imgss):
                    message['imgs'] = imgss
        except Exception as e:
            pass
        print('\n')
        if dbhandler:
            dbhandler.insertx(message)
        message.clear()
        data = None
        time.sleep(0.1)
    except Exception as e:
        pass
