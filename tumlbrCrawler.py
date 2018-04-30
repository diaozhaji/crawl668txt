# coding=utf8

import os
import urllib.request
import newCrawler
import random
import time
import requests
import ssl

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# lelemmm
'''
cookie = 'tmgioct=5addf6436a01040118051320; rxx=p59kgzycv2.13k2x8zh&v=1; _ga=GA1.2.1437788940.1524495946; _gid=GA1.2.1780851914.1524495946; __utma=189990958.1437788940.1524495946.1524495946.1524495946.1; __utmb=189990958.0.10.1524495946; __utmc=189990958; __utmz=189990958.1524495946.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; language=%2Czh_CN; logged_in=1; pfx=c684e8533ff7d1606938f1aff15c473686024f2dff105753ffa776f8ed684fda%230%232907407940'
headers = {'User-Agent': ua,
           'Referer': 'http://lelemmm.tumblr.com/',
           'Cookie': cookie,
           'Host': 'lelemmm.tumblr.com',
           'Proxy-Authorization': 'Basic ZGlhb3poYWppOmRpYW96aGFqaTAx'}
'''
# image
cookie = 'tmgioct=5addf6436a01040118051320; rxx=p59kgzycv2.13k2x8zh&v=1; _ga=GA1.2.1437788940.1524495946; _gid=GA1.2.810339238.1525019071; __utma=189990958.1437788940.1524495946.1525019073.1525019313.5; __utmb=189990958.0.10.1525019313; __utmc=189990958; __utmz=189990958.1525019313.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; language=%2Czh_CN; logged_in=1; pfx=a29642a56471431f683d7ddd0d04698a5ec300eed8f7bdc79df0bcc6f5d27acb%230%236853838504; __gads=ID=1848ffb51c5ba831:T=1525019451:S=ALNI_MbDD9p77TNYkLulOQFSeHtxfS79LQ'
headers = {'method': 'GET',
           'User-Agent': ua,
           'authority': '78.media.tumblr.com',
           'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
           'Referer': 'https://www.tumblr.com/dashboard',
           'Cookie': cookie}



def get_tumblr_html(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=20).read().decode('gbk', 'ignore')
        # print(data)
        return data

    except Exception as e:
        print(e)


def random_sec(min, max):
    r = random.randint(min, max)
    print('sleep ' + str(r) + ' s')
    return r


def get_img(url):
    try:
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=20, context=context).read()
        # print(data)
        return data

    except Exception as e:
        print(e)


def save_img(url, target):
    # img = get_img(url)
    # newCrawler.write_file(target, img, 'w+')
    # urllib.request.urlretrieve(url, target)
    # print(url + ' finish')
    # time.sleep(random_sec())
    data = get_img(url)
    if data is not None:
        newCrawler.write_img(target, data)
    time.sleep(random_sec(0, 5))


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
        time.sleep(random_sec(2, 7))


def main():
    # crawler_tumblr('kotori950422', 1, 3)
    crawler_tumblr('lelemmm', 250, 300)


if __name__ == '__main__':
    main()
