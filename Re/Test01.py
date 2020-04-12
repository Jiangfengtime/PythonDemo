import re

print(re.search(r"Fishc", "www.Fishc.com"))

# .:匹配除换行符之外的任何字符
print(re.search(r"Fish.", "www.Fishc.com" ))
# 如果要匹配".",则需要在其前面加上"\"
print(re.search(r"Fishc\.", "www.Fishc.com" ))

# \d :匹配数字
print(re.search(r"\d\d\d", "www.360.com"))

# []:
print(re.search(r"[aeiou]", "www.Fishc.com"))
print(re.search(r"[A-Z]", "www.Fishc.com"))
print(re.search(r"[1-9]", "www.360.com"))

# {}:重复次数
print(re.search(r"ab{3}c", "abbaacaabbbc"))
print(re.search(r"ab{3,5}c", "abbaacaabbbbc"))
# 匹配 0 - 255
print(re.search(r"^([0-1]?\d?\d|2[0-4]\d|25[0-5])$", '255'))

print(re.search(r"(hello)\1\.\1", "hellohello.hello"))
print(re.search(r"[.]", "www.baidu.com"))
print(re.search(r"\.", "www.baidu.com"))

print(re.findall(r"[0-9]", "www.360.com"))




