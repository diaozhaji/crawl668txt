# coding=utf-8

# from lxml import etree
from bs4 import BeautifulSoup
import re
from peewee import *
import newCrawler

db = SqliteDatabase('sis_novel.db')


class Novel(Model):
    name = CharField()
    url = CharField()
    category = CharField()

    class Meta:
        database = db  # This model uses the "people.db" database.


def write_file(path, data, mode):
    f = open(path, mode)
    f.write(data)
    f.close()


db.connect()
db.create_tables([Novel])

htmls_wxzz = './sis_txt/wxzz/'
htmls_ycrs = './sis_txt/ycrs/'

file_name = htmls_wxzz + "3.html"

root_url = 'http://sis001.com/forum/'


def print_a_text(name):
    soup = BeautifulSoup(open(name, 'r', encoding='utf-8'), 'html.parser')
    # print(soup.prettify())
    for link in soup.select('tbody > tr > th > span'):
        # print(link)
        a = link.select('a')
        for b in a:
            if len(b.text) > 3:
                print(b.text)


def save_novel(name):
    soup = BeautifulSoup(open(name, 'r', encoding='utf-8'), 'html.parser')
    # print(soup.prettify())
    # for link in soup.select('form > table > tbody'):
    #     print(link)
    thread = soup.find_all(href=re.compile("thread"))
    for t in thread:
        if '【' in t.text:
            n = Novel(name=t.text, url=root_url + t['href'], category='wxzz')
            # print(t['href'])
            # print(t.text)
            n.save()


def parse_novel_name_form_html(start, end, dir):
    for i in range(start, end):
        filename = dir + str(i) + '.html'
        print(filename)
        save_novel(filename)
        print("#####################")


def parse_text_from_html(name):
    print(name)
    soup = BeautifulSoup(open(name, 'r', encoding='utf-8'), 'html.parser')
    # print(soup)
    for c in soup.select('.t_msgfont'):
        if len(c) > 1000:
            print(c.text)


def main():
    # parse(1, 324, htmls_wxzz)
    # parse_novel_name_form_html(1, 130, htmls_ycrs)
    parse_text_from_html(newCrawler.html_content + "【神奇宝贝竟然是女性】（1-3）.html")


# for novel in Novel.select():
#     novel.delete_instance()
# print(novel.name)

# db.close()


if __name__ == '__main__':
    main()
