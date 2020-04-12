# ##########################列表#########################

# list1 = [1, 2, True, "String", [1, 2, 3]]
# for i in list1:
#     print(i)

# language = ["HTML", "CSS", "JavaScript"]
# print(language)

# ###########################元素添加############################
# 向列表末尾追加元素:append extend

# language = ["HTML", "CSS", "JavaScript"]
# language.append("Python")
# language.extend("Java")
# print(language)

# append和extend都可以扩充列表,而且只能传一个参数
# 但是append针对的是元素,而extend针对的是列表
# 把列表当成一个元素添加
# language = ["HTML", "CSS", "JavaScript"]
# language.append(["MySql", "Hive"])
# print(language)
# 把列表中的元素单独添加
# language.extend(["MySql", "Hive"])
# print(language)

# 在指定位置追加元素:insert
# language = ["HTML", "CSS", "JavaScript"]
# language.insert(0, "编程语言")
# print(language)

# ###########################元素获取############################
# language = ["HTML", "CSS", "JavaScript"]
# 获取列表中指定索引处的元素
# print(language[3])

# 获取列表中指定元素的下标索引:index
# print(language.index("HTML"))

# ###########################元素删除############################
# language = ['HTML', 'CSS', 'JavaScript', 'Python']
# print(language)

# 移除指定内容的元素:remove 如果元素不存在,则报错
# language.remove("HTML")
# print(language)

# 移除指定索引处的元素:del 如果下标不存在,则报错
# del language[2]
# del language # 删除整个列表
# print(language)

# 弹出指定下标的元素 pop ,默认是弹出列表尾部元素
# Lang = language.pop()
# print(Lang)
# print(language)

# Lang = language.pop(1)
# print(Lang)
# print(language)

# ###########################元素获取############################
# language = ['HTML', 'CSS', 'JavaScript', 'Python']
# 获取列表中指定下标范围内的元素.左闭右开
# print(language[1: 3])
# 如果是从0开始,可以省略不写,如果后面的参数是负数,则表示取到倒数第几个元素
# print(language[: -1])
# 列表直接赋值和拷贝的区别
# 如果是直接赋值给另一个列表,则修改原列表后赋值的列表会一同被修改
# 如果是拷贝给另一个列表,则修改原列表后拷贝的列表不会被修改

# #######################列表的拷贝和赋值########################
# language = ['HTML', 'CSS', 'JavaScript', 'Python']
# language1 = language
# language2 = language[:]
# language.pop()
# print(language)
# print(language1)
# print(language2)

# #######################列表的比较########################
# 先比较第一个元素,如果相等,则比较下一个元素
# list1 = [123, 343]
# list2 = [23, 343]
# print(list1 > list2)

# 列表相加
# list3 = list1 + list2
# print(list3)

# 列表数乘
# list4 = list1 * 3
# print(list4)

# 判断元素是否在列表中 in \ not in
# list1 = ['HTML', 'CSS', 'JavaScript', 'Python']
# print("HTML" in list1)
# print("html" not in list1)

# 注意: in 和not in 只能判断第一层中是否有该元素
# list2 = [123, 234, [345, 456], 567]
# print(345 in list2)
# print([345, 456] in list2)
# print(345 in list2[2])

# #######################列表的内置函数########################
list1 = ['HTML', 'CSS', 'JavaScript', 'Python']
# sort():排序.默认是从小到大排序
list1.sort()
print(list1)
# 如果添加reverse=True参数,则从大到小排序
list1.sort(reverse=True)
print(list1)


# count():列表中指定元素的个数
list2 = list1 * 3
print(list2)
print(list2.count("HTML"))
# index():元素在指定区间内第一次出现的索引位置.如果没有找到,则报错
print(list2.index("HTML", 2, 10))

# reverse():列表翻转
list1.reverse()
print(list1)

# copy():拷贝
list3 = list1.copy()
list4 = list1[:]
list1.append('Python')
print(list1)
print(list3)
print(list4)
