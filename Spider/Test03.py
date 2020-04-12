# 有道翻译
import json
import urllib.request
import urllib.parse
import time

while True:

    content = input("请输入要翻译的内容(输入wq提出程序)：")
    if content == 'wq':
        break
    # 设置Url-agent。方式一：通过Request的headers参数修改
    # head = {
    #     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    #                   "(KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}

    # 注意复制进来的url要删除url中的"_o"，不然会报错
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        "i": content,
        "from": 'AUTO',
        "to": 'AUTO',
        "smartresult": 'dict',
        "client": 'fanyideskweb',
        "salt": '15849243408629',
        "sign": '7f97322878148f80d635dc1bcab9a3f1',
        "ts": '1584924340862',
        "bv": '35242348db4225f3512aa00c2f3e7826',
        "doctype": 'json', "version": '2.1',
        "keyfrom": 'fanyi.web',
        "action": 'FY_BY_CLICKBUTTION'
    }

    data = urllib.parse.urlencode(data).encode("UTF-8")
    # 设置Url-agent。方式一：通过Request的headers参数修改
    # req = urllib.request.Request(url, data, head)

    # 设置Url-agent。方式二：通过Request.add_header()方法修改
    req = urllib.request.Request(url, data)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                 "(KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36")
    response = urllib.request.urlopen(req)

    html = response.read().decode("UTF-8")
    target = json.loads(html)
    result = target['translateResult'][0][0]['tgt']
    print("翻译结果为：%s" % result)

    # 隔五秒才能执行下一次
    # time.sleep(5)
