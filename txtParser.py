# -*- coding: utf-8 -*-
import os
import time
from lxml import etree

htmls_dir = './668txt/'
outFilePath = 'novel.txt'

count = 0
error = 0
f = open(outFilePath, "w")

for i in range(1, 180):
    filename = htmls_dir + str(i) + '.html'
    doc = etree.HTML(open(filename, 'r').read().decode('gb2312', 'ignore'))
    f.write('--------------This is  ' + str(i) + '  page!-----------------\n\n')
    try:
        count += 1
        for j in range(1, 21):
            node_p = doc.xpath("//div[@id='soft_content_" + str(j) + "']")
            node_title = doc.xpath("//span[@class='mainSoftName']/a")
            node_size = doc.xpath("//div[@class='mainListSize']")

            title = node_title[(j - 1)].text.encode('gb2312')
            size = node_size[(j)].text.encode('gb2312')
            p = node_p[0].text.encode('gb2312').strip()
            f.write(str(j) + ':' + size + '\n')
            f.write(title + '\n')
            f.write(p + '\n\n')
    except Exception, e:
        print e
        error += 1
    f.write('\n\n\n')

f.close()

print error
