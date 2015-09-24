# -*- coding: utf-8 -*-
import os
import time
from lxml import etree

htmls_dir = './sis_txt/rqyy/'
outFilePath = 'novel.txt'

url_root = 'http://38.103.161.185/forum/'

count = 0
error = 0
f = open(outFilePath,"w") 

for i in range(2,200):
	filename = htmls_dir+str(i)+'.html'
	print filename
	doc = etree.HTML(open(filename, 'r').read().decode('gbk','ignore'))
	f.write('--------------This is  '+str(i)+'  page!-----------------\n\n')
	'''
	try:
		count+=1
		for j in range(1,21):
			node_p = doc.xpath("//div[@id='soft_content_"+str(j)+"']")
			node_title = doc.xpath("//span[@class='mainSoftName']/a")
			node_size = doc.xpath("//div[@class='mainListSize']")

			title = node_title[(j-1)].text.encode('gb2312')
			size = node_size[(j)].text.encode('gb2312')
			p = node_p[0].text.encode('gb2312').strip()
			f.write(str(j)+':'+size+'\n')
			f.write(title+'\n')
			f.write(p+'\n\n')
	except Exception, e:
		print e
		error += 1
	f.write('\n\n\n')
	'''

	try:
		# 来自xpath helper
		node_titles = doc.xpath("//tbody/tr/th[@class='lock']/span/a")
		print len(node_titles)
		count = 0

		for j in range(0,len(node_titles)):
			if(len(node_titles[j].text)<3):
				print node_titles[j].text
				continue
			f.write(str(j) + node_titles[j].text.encode('utf-8').strip()+'\n')
			# 打印该节点信息
			node = node_titles[j]
			# print (node, node.tag, (node.items())) 
			# print node.get('href')
			f.write(url_root + node.get('href')+'\n\n')
			count = count + 1
		print '这页共 %s 个' % (count)

	except Exception, e:
		print e

f.close()

#print error

# 某novel内
# //tbody/tr[1]/td[@class='postcontent']/div[@class='postmessage defaultpost']/div/div


