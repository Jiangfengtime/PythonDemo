# 递归
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return n * func(n - 1)
# print(func(5))


# def fun2(num):
#     if num < 1:
#         print("输入错误")
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return fun2(num - 1) + fun2(num - 2)
#
#
# print(fun2(5))


# 汉罗塔
# def Hanoi(n, x, y, z):
#     if n == 1:
#         print(x, " --> ", z)
#     else:
#         # 将n-1个盘子移动到y上
#         Hanoi(n-1, x, z, y)
#         # 将第n个盘子移动到z上
#         print(x, " --> ", z)
#         # 最后将n-1个盘子移动到z上
#         Hanoi(n-1, y, x, z)
#
#
# num = input("请输入汉罗塔层数：")
# while True:
#     if not num.isdigit():
#         num = input("输入错误请重新输入：")
#     else:
#         break
# num = int(num)
# Hanoi(num, 'x', 'y', 'z')

















