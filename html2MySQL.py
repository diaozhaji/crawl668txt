# coding=utf8

from lxml import etree
import MySQLdb
import time

htmls_dir = './sis_txt/llmq/'
outFilePath = 'novel.txt'

# sis root
url_root = 'http://38.103.161.185/forum/'

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    cur = conn.cursor()
    conn.select_db('SisNovel')

    for i in range(1, 25):
        filename = htmls_dir + str(i) + '.html'
        print filename
        doc = etree.HTML(open(filename, 'r').read().decode('gbk', 'ignore'))

        # 来自xpath helper
        node_titles = doc.xpath("//tbody/tr/th[@class='lock']/span/a")
        print len(node_titles)

        for j in range(0, len(node_titles)):
            if (len(node_titles[j].text) < 6):
                print node_titles[j].text
                continue
            # f.write(str(j) + node_titles[j].text.encode('utf-8').strip() + '\n')
            # 打印该节点信息
            node = node_titles[j]
            # print (node, node.tag, (node.items()))
            # print node.get('href')
            # f.write(url_root + node.get('href') + '\n\n')
            # value = ["李彤彤", "jy", "http://hello.html", 1234, "llmq", time.time(), "1-22"]
            value = [
                node_titles[j].text.encode('utf-8').strip(),
                "",
                url_root + node.get('href'),
                0,
                "llmq",
                time.time(),
                ""]
            cur.execute('insert into novel values(null,%s,%s,%s,%s,%s,%s,%s)', value)

        print 'this page ' + str(i) + ' insert success'

    conn.commit()
    cur.close()
    conn.close()

except Exception, e:
    print e

# f.close()

# print error

# 某novel内
# //tbody/tr[1]/td[@class='postcontent']/div[@class='postmessage defaultpost']/div/div

# 查找title列中包含hello字符的项
# SELECT * FROM SisNovel.novel where title like "%hello%";
