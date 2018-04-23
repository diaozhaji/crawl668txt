# coding=utf8

import os
import urllib.request
import random
import time
import requests


# import requests


def write_file(path, data, mode):
    f = open(path, mode)
    f.write(data)
    f.close()


def get_headers():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
    ua = random.choice(user_agent_list)
    headers = {'User-Agent': ua, 'Referer': 'http://www.mzitu.com/'}
    return headers


def get_html(target_url):
    try:
        req = urllib.request.Request(target_url, headers=get_headers())
        data = urllib.request.urlopen(req, timeout=15).read().decode('gbk', 'ignore')
        # print(data)
        return data
        # the_page = response.read()
        # the_page = response.read().decode('gb2312', 'ignore').encode('gbk')
        # print(the_page)
        # return the_page

        # print('encoding:', response.encoding)
        # print('apparent_encoding:', response.apparent_encoding)
        # response.encoding = ('ISO-8859-1')
        #
        # print(requests.utils.get_encodings_from_content(response))
        # print('encoding :', response.encoding)
        # return response.text

    except Exception as e:
        print(e)
        return "wrong:url = " + target_url


html_dir_1 = './sis_txt/wxzz'
html_dir_2 = './sis_txt/ycrs'

html_content = "./sis_txt/content/"

if not os.path.isdir(html_dir_1):
    os.mkdir(html_dir_1)

if not os.path.isdir(html_dir_2):
    os.mkdir(html_dir_2)


# t_url = "http://www.baidu.com"
# write_file(html_dir + "/1.txt", get_html(t_url), 'w+')

# 文学作者
# for i in range(178, 324):
#     url = 'http://sis001.com/forum/forum-322-' + str(i) + '.html'
#     print(url)
#     write_file(html_dir_1 + "/" + str(i) + '.html', get_html(url), 'w+')
#     print('ok')
#     time.sleep(10)

def crawler(url, filename):
    print(url)
    print(filename)
    write_file(html_content + filename, get_html(url), 'w+')
    print('ok')
    time.sleep(10)


def main():
    print("we are in %s" % __name__)
    # 原创人生
    for i in range(70, 130):
        url = 'http://sis001.com/forum/forum-383-' + str(i) + '.html'
        print(url)
        write_file(html_dir_2 + "/" + str(i) + '.html', get_html(url), 'w+')
        print('ok')
        time.sleep(10)


if __name__ == '__main__':
    main()
