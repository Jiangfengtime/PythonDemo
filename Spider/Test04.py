# import urllib.request
# url = "http://www.ipdizhichaxun.com/"
# proxy_support = urllib.request.ProxyHandler({'http': '163.125.68.141:8888'})
# opener = urllib.request.build_opener(proxy_support)
# opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36")]
# urllib.request.install_opener(opener)
#
# response = urllib.request.urlopen(url)
# html = response.read().decode('utf-8')
# print(html)

import urllib.request
import random

url = 'http://www.ipdizhichaxun.com'

iplist = ['163.125.68.141:8888', '60.205.132.71:80', '116.196.85.166:3128']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
