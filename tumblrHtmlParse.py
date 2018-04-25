# coding=utf-8

from bs4 import BeautifulSoup
import os
import tumlbrCrawler


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


static_dir = './tumblr/lelemmm/images/'


def crawl_img(page):
    imgs_dir = static_dir + str(page)

    mkdir(imgs_dir)

    file_path = './tumblr/lelemmm/html/' + str(page) + ".html"
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
        print(img_path)
        if os.path.exists(img_path):
            continue
        tumlbrCrawler.save_img(item, img_path)
        # print(index)
    # return index


# target_url = tumlbrCrawler.html_dir_1 + '/images/tumblr_p6dthfWnFU1tkv6t1o4_1280.jpg'
# img_url = 'https://78.media.tumblr.com/1ba516b65d56e167f7dd0d2d8dcba84a/tumblr_p6dthfWnFU1tkv6t1o4_1280.jpg'
# tumlbrCrawler.save_img(img_url, target_url)

for i in range(20, 26):
    try:
        crawl_img(i)

    except Exception as e:
        print(e)
