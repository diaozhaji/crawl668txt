# coding=utf-8

from bs4 import BeautifulSoup
import os
import tumlbrCrawler
import time


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')


def crawl_img(author, page):
    static_dir = './tumblr/' + author + '/images/'

    imgs_dir = static_dir + str(page)

    mkdir(imgs_dir)

    file_path = './tumblr/' + author + '/html/' + str(page) + ".html"
    print(file_path)

    img_list = []
    soup = BeautifulSoup(open(file_path, 'r', encoding='utf-8'), 'html.parser')
    i = 0
    for imgs in soup.select('.pxu-photo img'):
        # print(imgs.attrs['data-highres'])
        img_list.insert(i, imgs.attrs['data-highres'])

    index = 0
    for item in img_list:
        # print(item)
        name = str.split(item, '/')[4]
        index = index + 1
        img_path = static_dir + str(page) + '/' + name
        print('存到:' + img_path)
        if os.path.exists(img_path):
            continue
        print('需要爬:' + item)
        tumlbrCrawler.save_img(item, img_path)
        # print(index)
    time.sleep(tumlbrCrawler.random_sec(15, 20))
    # return index


# target_url = tumlbrCrawler.html_dir_1 + '/images/tumblr_p6dthfWnFU1tkv6t1o4_1280.jpg'
# img_url = 'https://78.media.tumblr.com/1ba516b65d56e167f7dd0d2d8dcba84a/tumblr_p6dthfWnFU1tkv6t1o4_1280.jpg'
# tumlbrCrawler.save_img(img_url, target_url)

def parse_tumblr_and_get_imgs(author, start, end):
    for i in range(start, end):
        try:
            crawl_img(author, i)

        except Exception as e:
            print(e)


parse_tumblr_and_get_imgs('lelemmm', 150, 180)
# parse_tumblr_and_get_imgs('kotori950422', 1, 3)
