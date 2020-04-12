# # ###########################元组#########################
# tuple1 = (1, 2, 3, 4, 5, 6)
# print(tuple1)
# print(tuple1[2])
# print(tuple1[3:])
#
# # 判断是不是元组的关键是',' 而不是"()"
# tuple2 = ()
# print(type(tuple2))
# # 如果元组中只有一个元素,则需要在其后面加上一个逗号","
# tuple3 = (1)
# print(type(tuple3))
# tuple4 = (1,)
# print(type(tuple4))
#
# # 元组不能被修改,所以"修改"和"更新"元组的本质是:
# # 重新创建一个元组来覆盖原有的元组
# # 添加元素
# language = ("HTML", "CSS", "JavaScript", "Python")
# language = language[:2] + ("Java",) + language[2:]
# print(language)
#

num = int(input("请输入一个整数:"))
i = 1
while i <= num:
    print(i)
    i += 1


num = int(input("请输入一个整数:"))
while num > 0:
    print(" " * num + "*" * num)
    num -= 1



