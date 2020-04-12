import urllib.request
# 获取网页地址
response = urllib.request.urlopen("http://www.fishc.com")
# 读取网页内容
html = response.read()
# 将网页内容按照指定的格式解码
html = html.decode("UTF-8")
print(html)
