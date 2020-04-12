import urllib.request
import os
import random


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0\
                   (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')

    proxies = ['163.125.68.141:8888', '60.205.132.71:80', '	114.249.114.63:9000']
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def get_page(url):  # 找到下一个页面的网址
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    c = html.find('<a href=', a)
    d = html.find('comments', a)
    next_page = html[c + 9:d + 8]
    return next_page


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a + 9:b + 4])
        else:
            b = a + 9
        a = html.find('img src=', b)
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open('http:' + each)
            f.write(img)


def download_mm(folder='ooxx', pages=10):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx/'
    for i in range(10):
        next_page = get_page(url)
        page_url = 'http:' + next_page
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)
        url = page_url


if __name__ == '__main__':
    download_mm()
