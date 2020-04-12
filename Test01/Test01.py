# print("----------鱼C工作室----------")

# input 中的内容为输入的提示；输入的内容则为其返回值
# temp = input('随便输入一个数字：')
# num = int(temp)
# if num == 8:
#     print("输入正确！")
# else:
#     print("输入错误！")


# BIF == Built-in function  内置函数
# 查看所有的内置函数：dir(__builtins__)
# print(dir(__builtins__))
# 查看内置函数的详细信息 help(内置函数)
# print(help(input))

# 原始字符串
# print("C:\now")
# 字符串前加上r，则不会转义字符
# print(r"C:\now")
# 注意：原始字符串不能以斜杠"\"结尾
# 解决思路一：在末尾加2个反斜杠，但最后一个不读取
# print(r"c:\Demo\\"[:-1])
# 解决思路二：字符串拼接
# print(r"c:\Demo" + "\\")

# 长字符串
# 长字符串以三个单引号或者双引号包围，相当于包围的内容原样输出
# str1 = """
# 锄禾日当午,
# 汗滴禾下土.
# 谁知盘中餐,
# 粒粒皆辛苦.
# """
# print(str1)

# 类型转换
# num = 15
# 转换成整型:int()
# print(int(num))

# 转换成浮点型:float()
# print(float(num))

# 转换成字符串:str()
# print(str(num))


# 获取变量类型:type()
# num = 15.0
# print(type(num))

# str2 = "15.0"
# print(type(str2))

# 判断变量的类型:isinstance(变量名,类型)
# print(isinstance(num, int))
# print(isinstance(num, float))

# 运算符: + - * /
# /:常规除法    //:取商
# ** 幂
# print(11 / 5)
# print(11 // 5)
# print(2 ** 5)

# num = input("输入成绩:")
# score = int(num)
# if 100 >= score >= 90:
#     print("等级为:A")
# elif 90 > score >= 80:
#     print("等级为:B")
# elif 80 > score >= 60:
#     print("等级为:C")
# elif 60 > score >= 0:
#     print("等级为:D")
# else:
#     print("输入错误")

# x, y = 7, 5
# if x < y:
#     small = x
# else:
#     small = y
# print(small)
# x, y = 7, 5
# small = x if x < y else y
# print(small)

# 断言:assert
# 如果assert后面的条件不满足时,会抛出异常
# assert 3 > 4

# for循环
str1 = "Hello World"
for i in str1:
    # end:指定分隔符,默认是以换行符分隔
    print(i, end=" ")

language = ["HTML", "CSS", "JavaScript", "Java", "PHP"]
for each in language:
    # len:判断元素的长度
    print(each, len(each))

# range(i):获取到0 -- i-1的整数数组.相当于:range(0, i)
# range(i, j):获取到i -- j-1的整数数组
# range(i, j, k):在i--j的整数数组中,以步长为k获取其中的元素
for i in range(5, 10, 2):
    print(i, end=" ")



















