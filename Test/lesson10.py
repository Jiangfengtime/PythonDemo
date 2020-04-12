# 有列表name = ['F', 'i', 'h', 'C'] ，如果小甲鱼想要在元素
# 'i' 和'h' 之间插入元素's'，应该使用什么方法来插入？

# name = ['F', 'i', 'h', 'c']
# name.insert(2, 's')
# print(name)

# list1 = [1, [1, 2, [' 小甲鱼']], 3, 5, 8, 13, 18]
# list1[1][2] = '小鱿鱼'
# print(list1)


# list1 = [1, 3, 5, 2, 5, 8, 4, 9]
# list1.sort()
# print(list1)
# 倒序
# list1.reverse()
# print(list1)
# list1.sort(reverse=True)

# print(list1)

# list1 = [i*i for i in range(10)]
# print(list1)

# old = [1, 2, 3, 4, 5]
# new = old
# print(id(new))
# print(id(old))
# old = [6]
# print(id(old))
# print(new)

# 字符串截取
# str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
# print(str1[16:29])
# print(str1[-45:-32])
# str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
# print(str1[0:-1:3])


# print("{1}".format("不打印", "打印"))
# print("{{1}}".format("不打印", "打印"))
# print('{0}{1:.2f}'.format('Pi = ', 3.1415))

# 进制转化
# while True:
#     num = input("请输入一个整数(输入Q退出)：")
#     if num != 'Q' and num != 'q':
#         while not num.isdigit():
#             num = input("输入的格式数据有误，请重新输入：")
#         num = int(num)
#         print("十进制 --> 二进制：%d -> " % num, bin(num))
#         print("十进制 --> 八进制：%d -> 0%o" % (num, num))
#         print("十进制 --> 十六进制：%d -> 0x%x" % (num, num))
#     else:
#         print("退出！")
#         break


# print(max('I love FishC.com'))
# list1 = [1, 2, 4]
# print(sum(list1))


# 编写min():
# def MyMin(x):
#     min = x[0]
#     for i in x:
#         if i < min:
#             min = i
#     return min
#
# print(MyMin('1230456789'))


# 编写 sum()
# def MySum(list):
#     sum = 0
#     for each in list:
#         sum += each
#
#     return sum
#
#
# print(MySum([1, 3, 5, -2]))


# 编写一个函数power() 模拟内建函数pow() ，即power(x, y) 为计算并返回x 的y 次幂的
# 值。

# def dec(f):
#     n = 3
#
#     def wrapper(*args, **kw):
#         return f(*args, **kw) * n
#
#     return wrapper
#
#
# @dec
# def foo(n):
#     return n * 2
#
#
# print(foo(2))


# 编写程序，生成包含1000个0到100之间的随机整数，并统计每个元素的出现次数。（提示：使用集合。


# 编写程序，用户输入一个列表和2个整数作为下标，然后输出列表中介于2个下标之间的元素组成的子列表。
# 例如用户输入[1,2,3,4,5,6]和2,5，程序输出[3,4,5,6]。
# list1 = input("请输入一个列表:").split()
# num = input("请输入上下标:").split()
# # print(type(int(num[0])))
# list2 = list1[int(num[0]): int(num[1]) + 1]
# print(list2)
# # print(num[0], num[1])


# 设计一个字典，并编写程序，用户输入内容作为键，然后输出字典中对应
# 的值，如果用户输入的键不存在，则输出“您输入的键不存在！”
# dict1 = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five",
#          '6': "six", '7': "seven", '8': "eight", '9': "nine"}
# key = input("请输入字典键值：")
# if key in dict1.keys():
#     print(dict1[key])
# else:
#     print("您输入的键不存在！")


# 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果。
# import random
#
# list1 = [random.randint(0, 100) for i in range(20)]
# print(list1)
# list2 = list1[0: 10]
# list3 = list1[10:]
# list2.sort()
# list3.sort(reverse=True)
# list2.extend(list3)
# print(list2)

# a = ['name', 'age', 'sex']
# b = ['Dong', 38, 'Male']
# c = zip(a, b)
# print(dict(c))
#
# print({a[i]: b[i] for i in range(len(a))})

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(list1[::3])

# print([5 for i in range(10)])
#
#
# a = (1, 3, 5, 7)
# print(a[1])
# del a


# 分析逻辑运算符“or”的短路求值特性。
# or短路简单理解为：
#     当左侧为True时，无论右侧取什么值，最终结果都为True，
#     所以，python为了提高效率，就不会再计算右侧。
# print(3 or 4)   # 3


# 编写程序，运行后用户输入4位整数作为年份，判断其是否为闰年。
# 如果年份能被400整除，则为闰年；如果年份能被4整除但不能被100整除也为闰年。

# year = input("请输入年份：")
# while not year.isdigit():
#     year = input("格式不正确，请重新输入年份：")
# year = int(year)
# if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
#     print("%d年是闰年" % year)
# else:
#     print("%d年不是闰年" % year)


# 编写程序，生成一个包含50个随机整数的列表，然后删除其中所有奇数。（提示：从后向前删。）
# import random
# list1 = [random.randint(1, 100) for i in range(50)]
# print(list1)
# index = 49
# while index >= 0:
#     if list1[index] % 2 == 1:
#         list1.pop(index)
#     index -= 1
#
# print(list1)

# 编写程序，生成一个包含20个随机整数的列表，然后对其中偶数下标
# 的元素进行降序排列，奇数下标的元素不变。（提示：使用切片。）
# import random
# list1 = [random.randint(1, 100) for i in range(20)]
# print(list1)
# list2 = list1[::2]
# list2.sort(reverse=True)
# for i in range(0, len(list2), 1):
#     list1[2 * i] = list2[i]
# print(list1)

# 编写程序，用户从键盘输入小于1000的整数，对其进行因式分解。例如，10=2×5，60=2×2×3×5。
# num = input("请输入用于分解的数：")
# if not num.isdigit():
#     num = input("输入的内容格式有误，请重新输入：")
# num = int(num)


# 编写程序，至少使用2种不同的方法计算100以内所有奇数的和。
# sum = 0
# for i in range(1, 100, 2):
#     sum += i
# print(sum)
#
# sum = 0
# m = 0
# while m <= 100:
#     if m % 2 == 1:
#         sum += m
#     m += 1
# print(sum)









































