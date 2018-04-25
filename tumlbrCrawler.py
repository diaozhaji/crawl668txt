# coding=utf8

import os
import urllib.request
import newCrawler
import random
import time
import requests

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
cookie = 'tmgioct=5addf6436a01040118051320; rxx=p59kgzycv2.13k2x8zh&v=1; _ga=GA1.2.1437788940.1524495946; _gid=GA1.2.1780851914.1524495946; __utma=189990958.1437788940.1524495946.1524495946.1524495946.1; __utmb=189990958.0.10.1524495946; __utmc=189990958; __utmz=189990958.1524495946.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; language=%2Czh_CN; logged_in=1; pfx=c684e8533ff7d1606938f1aff15c473686024f2dff105753ffa776f8ed684fda%230%232907407940'
headers = {'User-Agent': ua,
           'Referer': 'http://lelemmm.tumblr.com/',
           'Cookie': cookie,
           'Host': 'lelemmm.tumblr.com',
           'Proxy-Authorization': 'Basic ZGlhb3poYWppOmRpYW96aGFqaTAx'}


def get_tumblr_html(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=20).read().decode('gbk', 'ignore')
        # print(data)
        return data

    except Exception as e:
        print(e)


def random_sec():
    r = random.randint(2, 7)
    print('sleep ' + str(r) + ' ms')
    return r


def get_img(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=20).read()
        print(data)
        return data

    except Exception as e:
        print(e)


def save_img(url, target):
    # img = get_img(url)
    # newCrawler.write_file(target, img, 'w+')
    urllib.request.urlretrieve(url, target)
    print(url + ' finish')
    time.sleep(random_sec())


def crawler_tumblr(author, start, end):
    print('get<' + author + '>\'s html from page:' + str(start) + ' to ' + str(end))
    host_url = 'http://' + author + '.tumblr.com/page/'
    # html_dir_1 = './tumblr/lelemmm'
    html_dir = './tumblr/' + author + '/html'
    if not os.path.isdir(html_dir):
        os.mkdir(html_dir)

    for i in range(start, end):
        url = host_url + str(i)
        print(url)
        file_path = html_dir + '/' + str(i) + '.html'
        print(file_path)
        data = get_tumblr_html(url)
        # print(data)
        if data is not None:
            newCrawler.write_file(file_path, data, 'w+')
        time.sleep(random_sec())


def main():
    crawler_tumblr('kotori950422', 5, 7)
    # crawler_tumblr('lelemmm', 120, 150)


if __name__ == '__main__':
    main()
