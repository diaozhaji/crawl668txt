# -*- coding: utf-8 -*-
from lxml import etree
import time

htmls_dir = './sis_txt/llmq/'
outFilePath = 'novel.txt'

# sis root
url_root = 'http://38.103.161.185/forum/'

count = 0
error = 0


# f = open(outFilePath, "w")

def time2stamp(hour_str):
    return int(time.mktime(time.strptime(hour_str, '%Y-%m-%d %H:%M')))


for i in range(3, 4):
    filename = htmls_dir + str(i) + '.html'
    print filename
    doc = etree.HTML(open(filename, 'r').read().decode('gbk', 'ignore'))
    # f.write('--------------This is  ' + str(i) + '  page!-----------------\n\n')

    try:

        # 来自xpath helper
        node_titles = doc.xpath("//tbody/tr/th[@class='lock']/span/a[1]")
        print len(node_titles)
        count = 0

        for j in range(0, len(node_titles)):
            if len(node_titles[j].text) < 3:
                # print node_titles[j].text
                continue
            # f.write(str(j) + node_titles[j].text.encode('utf-8').strip() + '\n')
            # 打印该节点信息
            node = node_titles[j]
            s_title_author = node.text.encode('utf-8').strip()
            s_list = s_title_author.split("作者：")
            if len(s_list) == 2:
                print s_list[0]
                print s_list[1]
            else:
                print s_list[0]

            # print (node, node.tag, (node.items()))
            # print node.get('href')
            # f.write(url_root + node.get('href') + '\n\n')
            count += 1
        # print '这页共 %s 个' % (count)
        if count != 45:
            print str(i) + '页数量不对'

        node_nums = doc.xpath("//tr/td[@class='nums']/em")
        for j in range(0, count):
            print node_nums[j].text

        nodes_last_post = doc.xpath("//tr/td[@class='lastpost']/em/a")
        for j in range(0, count):
            s = nodes_last_post[j].text
            print time2stamp(s)

    except Exception, e:
        print e


# f.close()

# print error

# 某novel内
# //tbody/tr[1]/td[@class='postcontent']/div[@class='postmessage defaultpost']/div/div
