# coding=utf-8

from peewee import *

import newCrawler
import SisHtmlParse

db = SqliteDatabase('sis_novel.db')


class Novel(Model):
    name = CharField()
    url = CharField()
    category = CharField()

    class Meta:
        database = db  # This model uses the "people.db" database.


# i = 0
# for novel in Novel.select():
#     # novel.delete_instance()
#     i = i + 1
#     print(novel.name)


def main():
    d = {}
    for n in Novel.select().where(Novel.name.contains('明雪仙子传')):
        d[n.url] = n.name

    for key in d:
        print(key, d[key])

        # newCrawler.crawler(key, d[key] + ".html")
        # SisHtmlParse.parse_text_from_html(newCrawler.html_content + d[key].name)


if __name__ == '__main__':
    main()
