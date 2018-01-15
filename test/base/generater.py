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

print(sys.getdefaultencoding())
from random import randint
reload(sys)
sys.setdefaultencoding('utf8')

print(sys.getdefaultencoding())

TYPES = {
    0: "基本",
    1:"个人求助",
    2:"常观世音微语录",
    3:"木轮",
    4:"网页链接",
    5:"起香",
    6:"放生报告",
    7:"派饭",
    8:"义工",
    9:"义诊",
    10:"捐赠",
    12:"纻麻兰若诗词????",
    11:"展开全文",
    11:"菩提不退"
}

from Sql import Mydb

def loadFenye(url,headers):
    request = urllib2.Request(url, headers=headers)
    texts = urllib2.urlopen(request)
    json_load = json.load(texts)
    data = json_load['data']
    return re.sub("(\\\)[rtn]*", '', data)

def getpager(headers=None, id=None, pager=1,fromz=None,dbhandler=None,endPager=sys.maxint):
    print('------------第' + str(pager) + '页开开始----------------').decode('gbk')
    if (headers is None):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'weibo.com',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Cookie': 'SINAGLOBAL=1510815786404.578.1515466720461; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whlmpw1aCEGIXSEPnjs_nRV5JpX5KMhUgL.Fo2RSo.Xeo.Reoz2dJLoIEBLxKMLBKqLB.-LxK-L1K2L1hnLxKMLBKqLB.-LxKqL1KqL1KMt; UOR=,,login.sina.com.cn; YF-Page-G0=f70469e0b5607cacf38b47457e34254f; ALF=1547512567; SSOLoginState=1515976568; SCF=Agq1re9TAoA5niMh9a3akxiE_e7DyTEVC4ydDcoiRPByntTWscYcq0tKBZwu0pk1BwdUDP6N8WnNYIIbU9izmRw.; SUB=_2A253X4cpDeRhGedG7VsV8ifEyT6IHXVULP_hrDV8PUNbmtBeLWzFkW9NUTixkg2pG_RV0TbnP40stw0NbNYCWkSz; SUHB=0FQax1DzFm8_i1; YF-V5-G0=c072c6ac12a0526ff9af4f0716396363; wb_cusLike_1869429822=N; _s_tentry=weibo.com; Apache=7010062560798.425.1515976587499; ULV=1515976587688:5:5:1:7010062560798.425.1515976587499:1515744629062'
        }
    patten = '<html><head>qqqq</head><body>%s</body></html>'
    url = u'https://weibo.com/{id_}?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={pager_}'.format(
        id_=id, pager_=pager)
    # print('>>>> '+url)
    request = urllib2.Request(url, headers=headers)
    texts = urllib2.urlopen(request).read()
    rexx = '(?:pl\.content\.homeFeed\.index).*?(?:Pl_Official_MyProfileFeed).*?"html":"(.*?)\"\}\)\</script\>'

    ss = re.search(rexx, texts).groups()[0]
    save = patten % ss

    save = re.sub("(\\\)[rtn]*", '', save).replace('<hml>', '<html>').replace('</hml>', '</html>')
    # print('>>> ' + save)
    # f = open('12.html', 'wb')
    # f.write(save)
    # f.flush()
    # f.close()
    soup = BeautifulSoup(save, 'lxml')

    allmessage = soup.find(class_='WB_feed WB_feed_v3 WB_feed_v4')
    print('---------------------------')
    time.sleep(randint(3, 5))
    print('---------------------------')
    pager1 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={pager}&pagebar=0&pl_name=Pl_Official_MyProfileFeed__24&id=1005051619101101&script_uri=/{name}&feed_type=0&pre_page={prepager}&domain_op=100505&__rnd=1515996882697'.format(
        pager=pager, name=id, prepager=pager)
    print(pager1)
    data = loadFenye(pager1, headers)
    beautiful_soup = BeautifulSoup(data,'lxml')
    list1=beautiful_soup.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like ')
    allmessage.contents.extend(list1)
    print('---------------------------')
    time.sleep(randint(2, 3))
    print('---------------------------')
    pager2 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={pager}&pagebar=1&pl_name=Pl_Official_MyProfileFeed__24&id=1005051619101101&script_uri=/{name}&feed_type=0&pre_page={prepager}&domain_op=100505&__rnd=1515996882697'.format(
        pager=pager, name=id, prepager=pager)
    print(pager2)
    data = loadFenye(pager2, headers)
    beautiful_soup2 = BeautifulSoup(data,"lxml")
    list2=beautiful_soup2.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like ')
    allmessage.contents.extend(list2)
    print('---------------------------')
    size = 0
    for eachmessage in allmessage.contents :
        if (type(eachmessage) is not bs4.element.Tag):
            continue
        message = {'come':fromz}
        try:
            namez = eachmessage.find(class_='WB_info').a.text
            if(namez not in fromz):
                continue
            message['fid'] = eachmessage['tbinfo'].split('=')[1]
            message['mid'] = eachmessage['mid']

            timeinfo = eachmessage.find(class_='WB_from S_txt2').find(name='a')
            message['timestr'] = timeinfo['title']
            print(message['timestr'])
            message['datelong'] = timeinfo['date']

            contentinfo = eachmessage.find(class_='WB_text W_f14')
            message['content'] = contentinfo.contents[0].strip().decode('utf8')

            if contentinfo.a:
                for hrefStr in contentinfo.a.contents:
                    if (type(hrefStr) is bs4.element.NavigableString):
                        message['hrefStr'] = getType(hrefStr.strip())
                        break
                message['href'] = contentinfo.a['href'].decode('utf8')

            message['category'] = getType(message['content'])
            boo=message['category'] == '基本'.decode('gbk').encode('utf8')
            try:
                if (boo and message['hrefStr']!='展开全文'.decode('gbk').encode('utf8')):
                    message['category'] = message['hrefStr']
            except Exception as e:
                pass
            imgsbox=eachmessage.find(class_='media_box')
            if(imgsbox):
                imgs=imgsbox.find_all(name='img')
                imgss = []
                if (imgs):
                    for img in imgs:
                        if (img['src']):
                            imgss.append(img['src'])
                if (imgss):
                    message['imgs'] = imgss
            print('\n')
            size += 1
            if dbhandler:
                dbhandler.insertx(message)
            time.sleep(0.1)
        except Exception as e:
            print("E=========================E"+e.message)
            pass

    print('------------第'+str(pager)+'页结束----------------'+str(size)).decode('gbk')
    print('\n')
    time.sleep(randint(2,3))
    if(size==0 or size>endPager):
       dbhandler.close()
       return
    getpager(headers=headers,id=id,pager=pager+1,fromz=fromz,dbhandler=dbhandler)
    return

def getType(type):
    for keys in TYPES.keys():
        strx=str(TYPES[keys]).decode('gbk')
        if strx in type:
            return TYPES[keys].decode('gbk').encode('utf8')
    return TYPES[0].decode('gbk').encode('utf8')

    if('个人求助' in type):
        a=1
    elif('常观世音微语录' in type):
        a=2
    elif('木轮' in type):
        a=3
    elif ('网页链接' in type):
        a = 4
    elif ('起香' in type):
        a = 4
    elif ('放生报告' in type):
        a = 4
    elif ('派饭' in type):
        a = 4
    else:
        a=0
    return TYPES[a]

if __name__ == '__main__':
    i1 = 'u/5549438666'
    i2 = 'manjuvimalakirti'
    dbhandler = Mydb()
    getpager(id=i2, pager=51,fromz="常觀世音微博".decode('gbk').encode('utf8'),dbhandler=dbhandler)

