import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/400/500")
# 等价于
# req = urllib.request.Request("http://placekitten.com/g/400/500")
# response = urllib.request.urlopen(req)

cat_img = response.read()

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_img)

# 获取访问的链接地址
print(response.geturl())

# 获取远程服务器信息
print(response.info())

# 获取状态码
print(response.getcode())
