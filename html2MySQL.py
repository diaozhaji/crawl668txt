# coding=utf8

from lxml import etree
import MySQLdb
import time


category = 'llmq'
htmls_dir = './sis_txt/' + category + '/'

outFilePath = 'novel.txt'

# sis root
url_root = 'http://38.103.161.185/forum/'


def time2stamp(hour_str):
    try:
        return int(time.mktime(time.strptime(hour_str, '%Y-%m-%d %H:%M')))
    except Exception, e:
        print e
        return 0


def get_novel_num(num_str):
    try:
        return int(num_str)
    except Exception, e:
        print e
        return 0


try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    cur = conn.cursor()
    conn.select_db('SisNovel')

    for i in range(2, 111):
        filename = htmls_dir + str(i) + '.html'
        print filename
        doc = etree.HTML(open(filename, 'r').read().decode('gbk', 'ignore'))

        node_titles = doc.xpath("//tbody/tr/th[@class='lock']/span/a[1]")
        node_nums = doc.xpath("//tr/td[@class='nums']/em")
        nodes_last_post = doc.xpath("//tr/td[@class='lastpost']/em/a")

        # page计数
        count = 0

        print 'node_titles大小为 %s' % len(node_titles)
        d = 0
        for j in range(0, len(node_titles)):
            print node_titles[j - d].text
            if len(node_titles[j - d].text) < 2:
                del node_titles[j - d]
                d += 1

        print 'now node_titles大小为 %s' % len(node_titles)
        print '第 %s 页共 %s 部小说' % (i, len(node_titles))

        for j in range(0, len(node_titles)):

            node = node_titles[j]
            s_title_list = node.text.encode('utf-8').strip()
            title_and_author = s_title_list.split("作者：")
            if len(title_and_author) == 2:
                print title_and_author[0]
                print '作者：' + title_and_author[1]
                value = [
                    title_and_author[0],
                    url_root + node.get('href'),
                    title_and_author[1],
                    get_novel_num(node_nums[j].text),
                    category,
                    time2stamp(nodes_last_post[j].text),
                    ""]
            else:
                print title_and_author[0]
                print '无作者'
                value = [
                    title_and_author[0],
                    url_root + node.get('href'),
                    "",
                    get_novel_num(node_nums[j].text),
                    category,
                    time2stamp(nodes_last_post[j].text),
                    ""]
            cur.execute('insert into novel values(null,%s,%s,%s,%s,%s,%s,%s)', value)

            count += 1

        print 'this page ' + str(i) + ' insert success'

        if count != 45:
            print 'but ' + str(i) + '页数量不对'
            print '这页共 %s 个' % (count)

    '''

    for j in range(0, count):
        print node_nums[j].text

    for j in range(0, count):
        s = nodes_last_post[j].text
        print time2stamp(s)

    node_titles = doc.xpath("//tbody/tr/th[@class='lock']/span/a")
    print len(node_titles)

    for j in range(0, len(node_titles)):
        if (len(node_titles[j].text) < 6):
            print node_titles[j].text
            continue
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
    '''

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
# 按nums 降序排列
# SELECT * FROM SisNovel.novel order by nums desc;
# 查询数据库中表的大小
# show table status from DBName where name = 'TBName';
# 清空表
# truncate novel;
# 查表某项有多少个
# select count(表中任意属性名，如name) from [table_name];
# 统计某分类下有多少个
# select count(*) from novel where category like 'rqyy';
