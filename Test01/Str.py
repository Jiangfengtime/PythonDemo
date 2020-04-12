str1 = "hello World"
# capitalize():把字符串首字母转变为大写字母
print(str1.capitalize())        # Hello world

# casefold(): 把字符串所有字符转为小写
print(str1.casefold())          # hello world

# center(width):将字符串居中,并使用空格填充至长度为width的新字符串
print(str1.center(20))          # '    hello World     '

# count(sub [,start [,end]]):返回sub字符串在自定范围内出现的次数

# endswith(sub [,start [,end]]):判断字符串是否以sub子串结尾
# startswith(sub [,start [,end]]):判断字符串是否以sub子串开头
print(str1.endswith("world"))   # False
print(str1.endswith("World"))   # True

# find(sub [,start [,end]]):检查指定子串所在位置.返回下标.如果没有找到则返回-1
# rfind(sub [,start [,end]]):默认从右往左开始查找
print(str1.find("orld"))        # 7

# index(sub [,start [,end]]):检查指定子串所在位置.返回下标.如果没有找到则报错
# rindex(sub [,start [,end]]):默认从右往左开始查找
print(str1.index("orld"))       # 7

# encode(encoding='utf-8',errors='strict'):将encoding指定为编码格式对字符串进行编码
str2 = "中国"
print(str2)                     # 中国
print(str2.encode("UTF-8"))     # b'\xe4\xb8\xad\xe5\x9b\xbd'

# expandtabs([tabsize=8]):把字符串中的tab符号(\t)转换为指定格式的空格.默认为8
str3 = "abc\tbcd\te"
print(str3.expandtabs(5))       # abc  bcd  e

# isalnum()  所有字符都是数字或者字母，为真返回 True，否则返回 False。
str1 = "1234abc"
str2 = "@we233"
print(str1.isalnum())   # True
print(str2.isalnum())   # False

# isalpha()   所有字符都是字母，为真返回 True，否则返回 False。
str1 = "1234abc"
str2 = "hello"
print(str1.isalpha())   # False
print(str2.isalpha())   # True

# isdigit()     所有字符都是数字，为真返回 True，否则返回 False。
str1 = "1234abc"
str2 = "123456"
print(str1.isdigit())   # False
print(str2.isdigit())   # True
# islower()    所有字符都是小写，为真返回 True，否则返回 False。
str1 = "hello"
str2 = "Hello"
print(str1.islower())   # True
print(str2.islower())   # False

# isupper()   只有第一个字符是大写,其余都是小写时返回 True，否则返回 False。
str1 = "hellO"
str2 = "HELLO"
print(str1.isupper())   # False
print(str2.isupper())   # True
# istitle()      所有单词都是首字母大写，为真返回 True，否则返回 False。
str1 = "HE"
str2 = "He"
print(str1.istitle())   # False
print(str2.istitle())   # True
# isspace()   所有字符都是空白字符，为真返回 True，否则返回 False。
str1 = "      "
str2 = ""
str3 = " '   "
print(str1.isspace())   # True
print(str2.isspace())   # False
print(str3.isspace())   # False

# join(sub):以字符串为分隔符,插入到sub字符串中的每一个字符中间
str1 = " "
sub = "hello"
print(str1.join(sub))   # h e l l o

# lstrip()去掉字符串中最左边的空格
# rstrip()去掉字符串中最右边的空格
# strip()去掉字符串中左右两边的空格
str1 = " hello "
print(str1.lstrip())    # 'hello '
print(str1.rstrip())    # ' hello'
print(str1.strip())     # 'hello'

# replace(old, new [, count]):用字符串new替换字符串old,
# 如果指定count,则替换次数不超过count,默认是全部替换
str1 = "hehehehehe"
print(str1.replace("e", "a"))                       # hahahahaha
print(str1.translate(str.maketrans("e", "a")))      # hahahahaha    [等价]
print(str1.replace("e", "a", 3))    # hahahahehe

# split(),按照指定字符切割字符串
str1 = "hello world"
print(str1.split())     # ['hello', 'world']
print(str1.split('e'))  # ['h', 'llo world']

str1 = "Hello World"
# lower():将字符串中的所有字符转换为小写
print(str1.lower())     # hello world
# supper():将字符串中的所有字符转换为大写
print(str1.upper())     # HELLO WORLD
# swapcase():将字符串中的大小写翻转
print(str1.swapcase())  # hELLO wORLD
# title() 将所有单词的首字母大写其余全变成小写
str1 = "hello world"
print(str1.title())     # Hello World


