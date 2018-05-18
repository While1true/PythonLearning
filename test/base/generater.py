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
    4:"善心莲心",
    5:"网页链接",
    6:"起香",
    7:"放生",
    8:"派饭",
    9:"义工",
    10:"义诊",
    11:"捐赠",
    11:"捐款",
    12:"纻麻兰若",
    13:"展开全文",
    14:"菩提不退"
}

from Sql import Mydb
lock=threading.Lock()
def loadFenye(url,headers):
    request = urllib2.Request(url, headers=headers)
    texts = urllib2.urlopen(request)
    json_load = json.load(texts)
    data = json_load['data']
    return re.sub("(\\\)[rtn]*", '', data)

def getpager(headers=None, id=None, pager=1,fromz=None,dbhandler=None,endPager=0,id2=None,rnd=None):
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
            'Cookie': 'SINAGLOBAL=1510815786404.578.1515466720461; UOR=,,www.baidu.com; wvr=6; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; ALF=1558145707; SSOLoginState=1526609707; SCF=Agq1re9TAoA5niMh9a3akxiE_e7DyTEVC4ydDcoiRPByfkTk5HsEazBy4LfiZ1q3BtZPQkTRDYAeJ68hNmEBaLM.; SUB=_2A253-kd8DeRhGedG7VsV8ifEyT6IHXVUjj-0rDV8PUNbmtBeLWPCkW9NUTixkpag2iuog9Ku81NuTchuXi1dIM8U; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whlmpw1aCEGIXSEPnjs_nRV5JpX5KzhUgL.Fo2RSo.Xeo.Reoz2dJLoIEBLxKMLBKqLB.-LxK-L1K2L1hnLxKMLBKqLB.-LxKqL1KqL1KMt; SUHB=0N2EPvXCxziLxg; YF-V5-G0=d45b2deaf680307fa1ec077ca90627d1; _s_tentry=login.sina.com.cn; Apache=8270940540922.78.1526609738658; ULV=1526609738715:20:4:4:8270940540922.78.1526609738658:1526550473138; YF-Page-G0=8ec35b246bb5b68c13549804abd380dc; WBStorage=5548c0baa42e6f3d|undefined'}
    patten = '<html><head>qqqq</head><body>%s</body></html>'
    # 'https://weibo.com/p/10080831a481db6e8571a9767e9f1d622892d2?current_page=6&since_id={%22last_since_id%22%3A4067354592027723%2C%22res_type%22%3A1%2C%22next_since_id%22%3A4061391054634665}&page=3#Pl_Third_App__11'
    url = u'https://weibo.com/{id_}?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={pager_}'.format(
        id_=id, pager_=pager)
    print('>>>> '+url)
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
    time.sleep(randint(4, 6))
    pager1 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={pager}&pagebar=0&pl_name=Pl_Official_MyProfileFeed__24&id={id2}&script_uri=/{name}&feed_type=0&pre_page={prepager}&domain_op=100505&__rnd={rnd}'.format(
        pager=pager, name=id,id2=id2,rnd=rnd, prepager=pager)
    print(pager1)
    data = loadFenye(pager1, headers)
    beautiful_soup = BeautifulSoup(data,'lxml')
    list1=beautiful_soup.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like ')
    allmessage.contents.extend(list1)
    time.sleep(randint(4, 6))
    pager2 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={pager}&pagebar=1&pl_name=Pl_Official_MyProfileFeed__24&id={id2}&script_uri=/{name}&feed_type=0&pre_page={prepager}&domain_op=100505&__rnd={rnd}'.format(
        pager=pager, name=id,id2=id2,rnd=rnd, prepager=pager)
    print(pager2)
    data = loadFenye(pager2, headers)
    beautiful_soup2 = BeautifulSoup(data,"lxml")
    list2=beautiful_soup2.find_all(class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_like ')
    allmessage.contents.extend(list2)
    size = 0
    for eachmessage in allmessage.contents :
        if (type(eachmessage) is not bs4.element.Tag):
            continue
        message = {'come':fromz}
        try:
            # namez = eachmessage.find(class_='WB_info').a.text
            # if(namez not in fromz):
            #     continue
            try:
                message['fid'] = eachmessage['tbinfo'].split('=')[1]
                message['mid'] = eachmessage['mid']
            except Exception as e:
                pass

            try:
                timeinfo = eachmessage.find(class_='WB_from S_txt2').find(name='a')
                message['timestr'] = timeinfo['title']
                message['href'] = timeinfo['href']
                message['datelong'] = timeinfo['date']
            except Exception as e:
                print(e.message)

            contentinfo = eachmessage.find(class_='WB_text W_f14')
            content=""
            try:
                for conent in contentinfo.contents:
                    try:
                        content += conent.strip().decode('utf8')
                    except Exception:
                        try:
                            content +=conent.get_text().decode('utf8')
                        except Exception:
                            pass
            except Exception as e:
                try:
                    conent+=contentinfo.contents[0];
                except Exception:
                    pass
            message['content'] = content


            try:
                try:
                    if contentinfo.a:
                        for hrefStr in contentinfo.a.contents:
                            if (type(hrefStr) is bs4.element.NavigableString):
                                message['hrefStr'] = getType(hrefStr.strip())
                                break
                except Exception:
                    pass
                    # message['href'] = contentinfo.a['href'].decode('utf8')
                if(fromz=='学诚法师微博'.decode('gbk').encode('utf8')):
                    message['category'] ='学诚法师微博'.decode('gbk').encode('utf8')
                else:
                    message['category'] = getType(message['content'])
                    boo = message['category'] == '基本'.decode('gbk').encode('utf8')
                    try:
                        if (boo and message['hrefStr']!='展开全文'.decode('gbk').encode('utf8')):
                            message['category'] = message['hrefStr']
                    except Exception:
                        pass
                imgsbox=eachmessage.find(class_='media_box')
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
            size += 1
            if dbhandler:
                if(message['content']!=""):
                    dbhandler.insertx(message)
            message.clear()
            data=None
            time.sleep(0.1)
        except Exception as e:
            print(str(pager)+"E=========================E"+e.message)
            pass

    print('------------第'+str(pager)+'页结束----------------'+str(size)).decode('gbk')
    print('\n')
    time.sleep(randint(4,12))
    if(size==0 or pager>=endPager):
       return
    getpager(headers=headers,id=id,pager=pager+1,fromz=fromz,dbhandler=dbhandler,endPager=endPager,id2=id2,rnd=rnd)
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
# 'https://weibo.com/p/10080831a481db6e8571a9767e9f1d622892d2/emceercd?current_page=3&since_id=44&page=3#Pl_Third_App__46'
# 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100808&current_page=7&since_id=104&page=3&pagebar=0&tab=emceercd&pl_name=Pl_Third_App__46&id=10080831a481db6e8571a9767e9f1d622892d2&script_uri=/p/10080831a481db6e8571a9767e9f1d622892d2/emceercd&feed_type=1&pre_page=3&domain_op=100808&__rnd=1516160841956'
# 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100808&current_page=8&since_id=119&page=3&pagebar=1&tab=emceercd&pl_name=Pl_Third_App__46&id=10080831a481db6e8571a9767e9f1d622892d2&script_uri=/p/10080831a481db6e8571a9767e9f1d622892d2/emceercd&feed_type=1&pre_page=3&domain_op=100808&__rnd=1516160801500'

# 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100808&current_page=4&since_id=59&page=2&pagebar=0&tab=emceercd&pl_name=Pl_Third_App__46&id=10080831a481db6e8571a9767e9f1d622892d2&script_uri=/p/10080831a481db6e8571a9767e9f1d622892d2/emceercd&feed_type=1&pre_page=2&domain_op=100808&__rnd=1516160907286'
    maps=[{'i2' : 'u/5549438666','id2': 1005055549438666,'rnd': 1516069137716,'name':'纻麻兰若-常观世音法语集'},
          {'i2' : 'manjuvimalakirti','id2': 1005051619101101,'rnd': 1515996882697,'name':'常觀世音微博'},
          {'i2' : 'u/2405056755','id2': 1005052405056755,'rnd': 1516069343040,'name':'善心莲心微博'},
          {'i2': 'xuecheng', 'id2': 1005051218353337, 'rnd': 1526610229055, 'name': '学诚法师微博'}
        # ,
        #   {'i2' : 'u/2405056755','id2': '10080831a481db6e8571a9767e9f1d622892d2','rnd': 1516149484121,'name':'纻麻兰若诗词'}
          ]
    for chose in range(0,maps.__len__()):
        if(chose!=3):
            continue
        i2=maps[chose]['i2']
        id2 = maps[chose]['id2']
        rnd = maps[chose]['rnd']
        name = maps[chose]['name']

        threads = []
        dbs = []
        step = 40
        for i in range(742, 781, step):
            print(i)
        # "常觀世音微博".decode('gbk').encode('utf8')
            dbhandler = Mydb()
            dbs.append(dbhandler)
            thread = threading.Thread(target=getpager, args=(
            None, i2, i, name.decode('gbk').encode('utf8'), dbhandler, i + step - 1, id2, rnd))
            threads.append(thread)
        for tt in threads:
            tt.start()
            time.sleep(0.5)
        for tt in threads:
            tt.join()
        for dbz in dbs:
            dbz.close()
    # getpager(id=i2, pager=51,fromz="常觀世音微博".decode('gbk').encode('utf8'),dbhandler=dbhandler)
