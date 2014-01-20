# -*- coding: utf8 -*-

import mechanize
import cookielib
import time
import re
from BeautifulSoup import BeautifulSoup


#初始化mechanize，相当于浏览器
def init():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()

    br.set_cookiejar(cj)
    br.set_handle_equiv(True)  
    br.set_handle_gzip(False)  
    br.set_handle_redirect(True)
    br.set_handle_referer(True)  
    br.set_handle_robots(False)  
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
    br.set_debug_http(False)  
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')] 
    print 'br initialized.'



#输入url，返回该url的html，data
def contentPageCrawler(url):
    global br
    init()
    data = None
    try:
        print 'now read', url
        res = br.open(url)
        data = res.read()
        print 'read OK'
        return data
    except Exception, e:
        print "line 45  contenPageCrawler ", e
        return None
    
#写入文件,用a方式
def writeToTxt(path,data,mode):
    f = file(path,mode);
    f.write(data+'\n')
    f.close();

#读取我要的数据
def loadTitle(doc):
    soup = BeautifulSoup(''.join(doc))
    mTitles = soup.findAll("span", { "class" : "mainSoftName" })
    for i in range(0,len(mTitles)):
        print mTitles[i].a['title']
        myid = 'soft_content_' + str(i+1)
        #print 'now '+ myid
        content = soup.find(id = myid)
        print content.text
        print '\n'

    
#执行的操作
for i in range(2,3):
    url = 'http://www.wi668.com/soft/html/list1-'+str(i)+'.html'
    content = contentPageCrawler(url)
    writeToTxt('e:\\temp.txt',content,'w')
    
    #writeToTxt('e://a.txt',content)
    print str(i)+'this page OK'
    time.sleep(3)
else:
    print 'laod txt finish'




