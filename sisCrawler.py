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

htmls_dir = './sis_txt'
if not os.path.isdir(htmls_dir):
	os.mkdir(htmls_dir)

for i in range(80,82):
	url = 'http://38.103.161.185/forum/forum-279-'+str(i)+'.html'
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
	time.sleep(5)



