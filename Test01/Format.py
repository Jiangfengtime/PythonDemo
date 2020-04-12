str1 = "{0} love {1}.{2}"
print(str1.format("I", "Fishc", "com"))

str2 = "{a} love {b}.{c}"
print(str2.format(a="I", b="Fishc", c="com"))

# 冒号表示格式化符号的开始
print("{0:.1f}{1}".format(27.654, "GB"))

# %c  格式化字符及其 ASCII 码
print('%c' % 97)                    # a
print('%c %c %c' % (97, 98, 99))    # a b c
# %s  格式化字符串
# %d  格式化整数
print('%d + %d = %d' % (4, 5, 4 + 5))

# 进制转换
num = 255
# %o  格式化无符号八进制数
# #%o  格式化有符号八进制数
print("%o" % num)
print("%#o" % num)

# %x  格式化无符号十六进制数
print("%x" % num)
print("%#x" % num)
# %X  格式化无符号十六进制数（大写）
print("%X" % num)

PI = 3.141592653
# %f  格式化浮点数字，可指定小数点后的精度
# m.n中的m表示最终的数字保留m个字符;n表示保留多少位小数
# 如果数字的位数小于m位,则在其最前面添加空格补位
print("%3.2f" % PI)
# %e  用科学计数法格式化浮点数
# %E  作用同 %e，用科学计数法格式化浮点数
# %g  根据值的大小决定使用 %f 或 %e
# %G  作用同 %g，根据值的大小决定使用 %f 或者 %E
