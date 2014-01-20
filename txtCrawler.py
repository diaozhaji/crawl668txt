#coding=utf8

import time
import urllib2
import socket
import cookielib
import sys
import os

def writeTo(path,data,mode):
    f = file(path,mode)
    f.write(data)
    f.close()


start_time = time.time()

socket.setdefaulttimeout(100)


cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

htmls_dir = './668txt'
if not os.path.isdir(htmls_dir):
	os.mkdir(htmls_dir)

for i in range(1,3):
	url = 'http://www.txt668.com/soft/html/list7-'+str(i)+'.html'
	print url 
	path = '%s/%s.html' % (htmls_dir, i)
	print path
	try:
		data = urllib2.urlopen(url).read()
	except Exception, e:
		print url
		data = 'no data'
	writeTo(path, data, 'w+')
	end_time = time.time()
	print end_time - start_time
	time.sleep(10)



