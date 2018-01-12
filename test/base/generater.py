# encoding:utf_8
import urllib
import urllib2

import bs4
from bs4 import BeautifulSoup
import re
import time
import lxml
import sys
reload(sys)
print(sys.getdefaultencoding())
import json

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
}

from Sql import Mydb
def getpager(headers=None, id=None, pager=1,fromz=None,dbhandler=None):
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
            'Cookie': 'SINAGLOBAL=1510815786404.578.1515466720461; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whlmpw1aCEGIXSEPnjs_nRV5JpX5KMhUgL.Fo2RSo.Xeo.Reoz2dJLoIEBLxKMLBKqLB.-LxK-L1K2L1hnLxKMLBKqLB.-LxKqL1KqL1KMt; UOR=,,login.sina.com.cn; YF-Page-G0=ed0857c4c190a2e149fc966e43aaf725; ALF=1547280614; SSOLoginState=1515744616; SCF=Agq1re9TAoA5niMh9a3akxiE_e7DyTEVC4ydDcoiRPBybsr80jDzUWG8a9Bol6p4tGC-4osEJVrdyWApkFpF6Qk.; SUB=_2A253XB04DeRhGedG7VsV8ifEyT6IHXVUKAnwrDV8PUNbmtBeLVXAkW9NUTixkjtWI8BdOrcto17WaOmsyjQHlBS4; SUHB=0D-0B2cM2CoXCl; _s_tentry=login.sina.com.cn; Apache=9872880251384.654.1515744628765; ULV=1515744629062:4:4:4:9872880251384.654.1515744628765:1515657426358; YF-V5-G0=020421dd535a1c903e89d913fb8a2988; wb_cusLike_1869429822=N'
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
    size = 0
    for eachmessage in allmessage.contents:
        if (type(eachmessage) is not bs4.element.Tag):
            continue

        message = {'come':fromz}
        try:
            message['fid'] = eachmessage['tbinfo'].split('=')[1]
            message['mid'] = eachmessage['mid']

            timeinfo = eachmessage.find(class_='WB_from S_txt2').find(name='a')
            message['timestr'] = timeinfo['title']
            message['datelong'] = timeinfo['date']

            contentinfo = eachmessage.find(class_='WB_text W_f14')
            message['content'] = contentinfo.contents[0].strip().decode('utf8')

            if contentinfo.a:
                for hrefStr in contentinfo.a.contents:
                    if (type(hrefStr) is bs4.element.NavigableString):
                        message['hrefStr'] = getType(hrefStr.strip()).decode('gbk').encode('utf8')
                        break
                message['href'] = contentinfo.a['href'].decode('utf8')
                message['category']=getType(message['content'])
                if(message['category']=='基本'):
                    message['category']=message['hrefStr'];
            imgs=contentinfo.find_all(name='img')
            imgss = []
            if(imgs):
                for img in imgs:
                    if (img['src']):
                        imgss.append(img['src'])
            if(imgss):
                message['imgs']=imgss
            print('\n')
            size += 1
            if dbhandler:
                dbhandler.insertx(message)
            time.sleep(0.2)
        except Exception as e:
            print("E=========================E"+e.message)
            pass

    print('------------第'+str(pager)+'页结束----------------'+str(size)).decode('gbk')
    print('\n')
    time.sleep(6)
    dbhandler.close()
    # getpager(headers=headers,id=id,pager=pager+1,fromz=fromz)
    return

def getType(type):
    for keys in TYPES.keys():
        strx=str(TYPES[keys]).decode('gbk')
        if strx in type:
            return TYPES[keys]
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
    getpager(id=i2, pager=0,fromz="常观世音微博".decode('gbk').encode('utf8'),dbhandler=dbhandler)
