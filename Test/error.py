# import math
# def func(n):
#     count = 0
#     s = int(math.sqrt(n))
#     for i in range(2, s + 1):
#         if n % i == 0:
#             count += 2
#     if n == s * s:
#         count -= 1
#     count += 2
#     return count
# ipt = input().split()
# a = int(ipt[0])
# b = int(ipt[1])
# max = 0
# for i in range(a, b + 1):
#     m = func(i)
#     if m > max:
#         max = m
# print(max)


# 判断公差
# n = int(input())
# while n > 0:
#     ipt = input().split()
#     m = int(ipt[0])
#     for i in range(m):
#         ipt[i] = int(ipt[i])
#
#     list1 = ipt[1:]
#     list1.sort()
#     # print(list1)
#     计算公差
#     d = list1[1] - list1[0]
#     for i in range(1, m):
#         if list1[i] - list1[i - 1] != d:
#             print("no")
#             break
#         if i == m-1:
#             print("yes")
#     n -= 1







