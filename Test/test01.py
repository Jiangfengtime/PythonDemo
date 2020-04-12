# str1 = "China"
# str2 = ""
# for item in str1:
#     str2 += chr(ord(item) + 4)
# print(str2)

# 超时
# def func(year):
#     if year <= 3:
#         return year
#     else:
#         return func(year - 1) + func(year - 3)
#
#
# while True:
#     year = int(input())
#     if year != 0:
#         print(func(year))
#     else:
#         break

# year = 1
# while year <= 10:
#     print(func(year))
#     # year = int(input())
#     year += 1


# def f2c(f):
#     print("c=%.2f" % (5 * (f - 32) / 9))
#
#
# f = float(input())
# f2c(f)


# num = input().split()
# max = int(num[0])
# n = 0
# while n < 3:
#     if int(num[n]) > max:
#         max = int(num[n])
#     n += 1
#
# print(max)

# x = int(input())
# if x < 1:
#     print(x)
# elif 1 <= x < 10:
#     print(2*x-1)
# else:
#     print(3*x-11)

# score = int(input())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("E")


# num = input()
# length = len(num)
# print(length)
# for i in num:
#     print(i, end=' ')
# print()
# while length >= 1:
#     print(num[length - 1], end="")
#     length -= 1


# num = int(input())
# money = 0
#
# if num <= 100000:
#     money = num * 0.1
#
# if 100000 < num <= 200000:
#     money = (num - 100000) * 0.075 + 10000
#
# if 200000 < num <= 400000:
#     money = (num - 200000) * 0.05 + 17500
#
# if 400000 < num <= 600000:
#     money += (num - 400000) * 0.03 + 27500
#
# if 600000 < num <= 1000000:
#     money += (num - 600000) * 0.015 + 33500
# if num > 1000000:
#     money += (num - 1000000) * 0.01 + 39500
#
# print(int(money))


# ipt = input().split()
# m = int(ipt[0])
# n = int(ipt[1])
# if n > m:
#     m, n = n, m
# i = n
# j = m
# while True:
#     if n % i == 0 and m % i == 0:
#         # print(i)
#         break
#     i -= 1
#
# while True:
#     if j % m == 0 and j % n == 0:
#         # print(j)
#         break
#     j += 1
#
# print("%d %d" % (i, j))


# str1 = input()
# Ccount = 0
# Ncount = 0
# Scount = 0
# Ocount = 0
# for i in str1:
#     if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
#         Ccount += 1
#     elif '0' <= i <= '9':
#         Ncount += 1
#     elif ' ' == i:
#         Scount += 1
#     else:
#         Ocount += 1
#
# print("%d %d %d %d" % (Ccount, Ncount, Scount, Ocount))


# num = int(input())
# sum = 0
# flag = 1
# while flag <= num:
#     i = 1
#     m = 2
#     while i < flag:
#         m = 10 * m + 2
#         i += 1
#     sum += m
#     flag += 1
# print(sum)

# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return n * func(n - 1)
#
#
# num = int(input())
# sum = 0
# for i in range(1, num + 1):
#     sum += func(i)
#
# print(sum)

# sum = 0.0
# inp = input().split()
# a = int(inp[0])
# b = int(inp[1])
# c = int(inp[2])
# for i in range(1, a + 1):
#     sum += i
#
# for i in range(1, b + 1):
#     sum += i * i
#
# for i in range(1, c + 1):
#     sum += 1 / i
#
# print("%.2f" % sum)

# def func(m, n):
#     Msum = 0
#     Nsum = 0
#
#     for i in range(1, m):
#         if m % i == 0:
#             Msum += i
#
#     for i in range(1, n):
#         if n % i == 0:
#             Nsum += i
#
#     if m == Nsum and n == Msum:
#         print("YES")
#     else:
#         print("NO")
#
#
# num = int(input())
# for i in range(num):
#     ipt = input().split()
#     m = int(ipt[0])
#     n = int(ipt[1])
#     func(m, n)

# num = int(input())
# while num >= 1:
#     n = num % 10
#     num = int(num / 10)
#     print(n)


# def func(p):
#     if p == 1 or p == 0:
#         return 1
#     else:
#         return p * func(p - 1)
#
#
# list1 = []
#
# for n in range(1, 100001):
#     sum = 0
#     temp = n
#     while temp >= 1:
#         m = temp % 10
#         temp = temp // 10
#         sum += func(m)
#     if n == sum:
#         list1.append(n)
#
# list1 = [str(i) for i in list1]
# list1.sort()
# for i in list1:
#     print(i, end=" ")

# str1 = input()
# list1 = list(str1)
# str1 = ""
# for i in range(0, len(list1)):
#     if list1[i] == 'i':
#         list1[i] = 'l'
#     str1 += str(list1[i])
# print(str1)

# def func(n):
#     sum = 1
#     while n >= 1:
#         sum = sum * n
#         n -= 1
#     return sum
#
#
# print(func(1977))

# import math
# while True:
#     r = float(input())
#     v = 4/3 * math.pi * r ** 3
#     print("%.3f" % v)

# while True:
#     count = int(input())
#     sum = 1
#     for i in range(0, count - 1):
#         sum = (sum + 1) * 2
#     print(sum)


# import math
# while True:
#     ipt = input().split()
#     if ipt[0] == '0':
#         break
#
#     list1 = []
#     list2 = []
#     for i in range(1, len(ipt)):
#         m = int(ipt[i])
#         n = int(math.fabs(m))
#         if n not in list1:
#             list1.append(n)
#         list2.append(m)
#     list1.sort(reverse=True)
#     for i in range(0, len(list1)):
#         for j in range(0, len(list2)):
#             if math.fabs(list2[j]) == list1[i]:
#                 print(list2[j], end= ' ')
#                 break
#     print()


# ipt = input().split()
# m = int(ipt[0])
# n = int(ipt[1])
# sum = 0
# for i in range(m, n + 1):
#     if i % 3 == 1 and i % 5 == 3:
#         sum += i
#
# print(sum)

# import re

# num = int(input())
#
#
# while num > 0:
#     password = input()
#     type1 = 0
#     type2 = 0
#     type3 = 0
#     type4 = 0
#
#     if 8 <= len(password) <= 16:
#         for i in range(0, len(password)):
#             if 'a' <= password[i] <= 'z':
#                 type1 = 1
#             if '0' <= password[i] <= '9':
#                 type2 = 1
#             if 'A' <= password[i] <= 'Z':
#                 type3 = 1
#             if password[i] == '~' or password[i] == '!' or password[i] == '@' or password[i] == '#' or password[i] == '$' or password[i] == '%' or password[i] == '^':
#                 type4 = 1
#         if type1 + type2 + type3 + type4 >= 3:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")
#     num -= 1

# while True:
#     ipt = input().split()
#     n = int(ipt[0])
#     m = int(ipt[1])
#     list1 = [i for i in range(2, 2 + 2 * n, 2)]
#     index = 0
#     while index + m < n:
#         sum = 0
#         for i in range(0, m):
#             sum += list1[index]
#             index += 1
#         print(int(sum / m), end=" ")
#     else:
#         sum = 0
#         for i in range(index, n):
#             sum += list1[i]
#         print(int(sum / (n - index)))

# num = int(input())
# while num >= 1:
#     ipt = input().split()
#     AH = int(ipt[0])
#     AM = int(ipt[1])
#     AS = int(ipt[2])
#     BH = int(ipt[3])
#     BM = int(ipt[4])
#     BS = int(ipt[5])
#
#     H = AH + BH
#     M = AM + BM
#     S = AS + BS
#     if S >= 60:
#         S -= 60
#         M += 1
#     if M >= 60:
#         M -= 60
#         H += 1
#     print("%d %d %d" % (H, M, S))
#     num += 1

# num = int(input())
# map1 = {}
# max = 0
# while num >= 1:
#     m = int(input())
#     if m not in map1:
#         map1[m] = 1
#     else:
#         map1[m] = map1[m] + 1
#     num -= 1
# for i in map1:
#     if map1[i] > max:
#         key = i
#         max = map1[i]
# print(key)
# print(max)

# num = int(input())
# count = 0
# for f in range(1, 100):
#     for t in range(1, 100):
#         for o in range(1, 100):
#             if num == (f * 5 + t * 2 + o):
#                 count += 1
# print(count)

import math


# def func(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True
#
#
# while True:
#     num = int(input())
#     count = 0
#     for i in range(2, int(num / 2) + 1):
#         if func(i) and func(num - i):
#             count += 1
#     print(count)

# while True:
#     ipt = input().split()
#     num = int(ipt[0])
#     if num == 0:
#         break
#     count = 0
#     for i in range(1, num + 1):
#         ipt[i] = int(ipt[i])
#         if ipt[i] >= 100:
#             count += ipt[i] // 100
#             ipt[i] = ipt[i] % 100
#         if ipt[i] >= 50:
#             count += ipt[i] // 50
#             ipt[i] = ipt[i] % 50
#         if ipt[i] >= 10:
#             count += ipt[i] // 10
#             ipt[i] = ipt[i] % 10
#         if ipt[i] >= 5:
#             count += ipt[i] // 5
#             ipt[i] = ipt[i] % 5
#
#         if ipt[i] >= 2:
#             count += ipt[i] // 2
#             ipt[i] = ipt[i] % 2
#
#         if ipt[i] >= 1:
#             count += ipt[i] // 1
#             ipt[i] = ipt[i] % 1
#     print(count)


# while True:
#     str1 = input()
#     str2 = ""
#     if str1 == "End of file":
#         break
#     for i in range(len(str1)):
#         if str1[i] != ' ':
#             str2 += str1[i]
#     print(str2)

# while True:
#     string = input()
#     if string == "":
#         break
#     for i in range(len(string)):
#         if string[i] == '/' and string[i + 1] == '/':
#             if i != 0:
#                 print(string[0: i])
#             else:
#                 break
#     if "//" not in string:
#         print(string)


# while True:
#     m = int(input())
#     if m >= 0:
#         n = int(bin(m)[2:])
#     else:
#         n = - int(bin(m)[3:])
#     print("%d-->%d" % (m, n))

# def func(i, j):
#     if j == 0 or i == j:
#         return 1
#     else:
#         return func(i - 1, j - 1) + func(i - 1, j)
#
#
# while True:
#     num = int(input())
#     for i in range(num - 1, -1, -1):
#         print("   " * (num -1 - i), end="")
#         for j in range(0, i + 1):
#             print("%3d" % func(i, j), end='   ')
#         print()
#     print()

# while True:
#     string = input()
#     if string == "End of file":
#         break
#     string = string.upper()
#     print(string)

# def func(str1):
#     s = ""
#     for i in range(len(str1) -1, -1, -1):
#         s += str1[i]
#     if str1 == s:
#         print("Y")
#     else:
#         print("N")
#
#
# string = input()
# func(string)

# while True:
#     ipt = input().split()
#     length = len(ipt) - 1
#     max = int(ipt[0])
#     for i in range(length):
#         ipt[i] = int(ipt[i])
#         if ipt[i] > max:
#             max = ipt[i]
#     print(max)
#
# import math
# num = int(input())
# while num > 0:
#     r = float(input())
#     s = math.pi * r * r
#     print("%.6f" % s)

# str1 = input()
# str2 = ""
# length = len(str1)
# for i in range(length - 1, -1, -1):
#     str2 += str1[i]
#
# print(str2)

# num = int(input())
# while num > 0:
#     ipt = input().split()
#     m = int(ipt[0])
#     n = int(ipt[1])
#     if m + n <= 100:
#         print(m + n)
#     else:
#         print((m + n) % 100)
#     num -= 1

# while True:
#     ipt = input().split()
#     m = int(ipt[0])
#     n = int(ipt[1])
#     s1 = 0
#     s2 = 0
#     for i in range(m, n + 1):
#         if i % 2 == 0:
#             s1 += i * i
#         else:
#             s2 += i ** 3
#     print(s1, s2)

# while True:
#     start = input()
#     if start == 'ENDOFINPUT':
#         break
#     if start == 'START':
#         ipt = input()
#         end = input()
#         if end == "END":
#             for i in range(len(ipt)):
#                 if 'A' <= ipt[i] <= 'Z':
#                     # print(ord(ipt[i]))
#                     if ord(ipt[i]) - 5 >= ord('A'):
#                         print(chr(ord(ipt[i]) - 5), end="")
#                         # ipt[i] = chr(ord(ipt[i]) - 5)
#                     else:
#                         print(chr(ord(ipt[i]) + 21), end="")
#                         # ipt[i] = chr(ord(ipt[i]) + 21)
#                 else:
#                     print(ipt[i], end="")
#             print()

# def func(str1):
#     length = len(str1)
#     str2 = ""
#     for i in range(length-1, -1, -1):
#         str2 += str1[i]
#     if str1 == str2:
#         return True
#     else:
#         return False
#
#
# while True:
#     ipt = input()
#     length = len(ipt)
#     len2 = 0
#     for len1 in range(length, 0, -1):
#         for a in range(0, length - len1 + 1):
#             if func(ipt[a: a + len1]):
#                 # len2 = len1
#                 break
#         # if len2 != 0:
#         #     break
#         else:
#             continue
#         break
#     print(len1)


# import itertools
# num = int(input())
# ipt = input()
# string = ipt[0:num]
# # 全排列
# iter = itertools.permutations(ipt)
# # 转成集合
# set1 = set(iter)
# print(len(set1))


# while True:
#     score = int(input())
#     if score > 100 or score < 0:
#         print("Score is error!")
#     else:
#         if 90 <= score <= 100:
#             print("A")
#         elif 80 <= score < 90:
#             print("B")
#         elif 70 <= score < 80:
#             print("C")
#         elif 60 <= score < 70:
#             print("D")
#         else:
#             print("E")

# import itertools
# count = int(input())
# while count > 0:
#     ipt = input()
#
#     nums = ipt[::2]
#     list1 = list(itertools.permutations(nums))
#     count = 0
#     for i in list1:
#         str1 = ""
#         for j in i:
#             str1 += j
#         count += 1
#         print(str1, end=" ")
#         if count % 6 == 0:
#             print()
#     count -= 1
#     print()

# num = int(input())
# while num > 0:
#     ipt = input().split()
#     list1 = []
#     list1.insert(0, int(ipt[0]))
#     for i in range(1, len(ipt)):
#         ipt[i] = int(ipt[i])
#         if ipt[i] > int(ipt[0]):
#             list1.append(ipt[i])
#         else:
#             list1.insert(0, ipt[i])
#     for i in list1:
#         print(i, end=" ")
#     print()
#     num -= 1

# while True:
#     num1 = input().split()
#     m1 = int(num1[0])
#     n1 = int(num1[1])
#     # if m == 0 and n == 0:
#     #     break
#     ipt = input().split()
#     for i in range(m1):
#         ipt[i] = int(ipt[i])
#     for i in range(m):
#         if n < ipt[0]:
#             ipt.insert(0, n)
#         elif n > ipt[m - 1]:
#             ipt.append(n)
#         elif ipt[i] < n < ipt[i + 1]:
#             ipt.insert(i + 1, n)


# def func(n):
#     if n <= 3:
#         return n + 2
#     else:
#         return func(n - 1) + func(n - 2) + func(n - 3)
#
#
# num = int(input())
# print(func(num))

# num = int(input())
# list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(1, num + 1):
#     while i >= 10:
#         m = i % 10
#         list1[m] += 1
#         i = int(i / 10)
#     if i > 0:
#         list1[i] += 1
#
# for i in range(10):
#     print(list1[i])

# while True:
#     ipt = input().split()
#     m = int(ipt[0])
#     n = int(ipt[1])
#     if m == 0 and n == 0:
#         break
#     s = m * 100
#     for i in range(s, s + 100):
#         if i % n == 0:
#             t = i - s
#             if t < 10:
#                 print("%d%d" % (0, t), end=" ")
#             else:
#                 print(t, end=" ")
#     print()

# while True:
# num = int(input())
#
# count = 0
# for i in range(2, num + 1):
#     # while i > 1:
#     if i % 7 == 0:
#         count += 1
#         continue
#     while i > 1:
#         t = i % 10
#         if t == 7:
#             count += 1
#             break
#         i = int(i / 10)
#
#
# print(count)


# count = int(input())
# while count > 0:
#     num = int(input())
#     if num % 2 == 0:
#         print(4)
#     else:
#         print(num + 3)
#     count -= 1
# '15/12/1999', '02/12/2004', '10/21/2003', '10/22/2003',  '11/30/2005', '12/31/2005'


# items = []
# temps = []
#
# while True:
#     ipt = input()
#     if not ipt:
#         break
#     items.append(ipt)
#
#
# for item in items:
#     lists = item.split('/')
#     lst = lists[2] + lists[0] + lists[1]
#     temps.append(lst)
# temps.sort()
# for temp in temps:
#     y = temp[0:4]
#     m = temp[4:6]
#     d = temp[6:8]
#     lst = m + "/" + d + "/" + y
#     print(lst)


# ipt = input().split()
# m = int(ipt[0])
# n = int(ipt[1])
# if n > m:
#     m, n = n, m
# for i in range(m, n * m + 1, m):
#     if i % n == 0:
#         print(i)
#         break

# def func(m, n):
#     if n == 0 or m == n:
#         return 1
#     else:
#         return func(m - 1, n - 1) + func(m - 1, n)
#
#
# nums = input().split()
# for item in nums:
#     n = int(item)
#     for j in range(0, n):
#         for i in range(0, j + 1):
#             print(func(j, i), end=" ")
#         print()
#     print()

# while True:
#     ipt = input()
#     list1 = list(ipt)
#     list2 = []
#     max = list1[0]
#     string = ""
#     for i in range(len(list1)):
#         if list1[i] == max:
#             list2.append(i)
#         elif list1[i] > max:
#             max = list1[i]
#             list2.clear()
#             list2.append(i)
#
#     for i in range(len(list2)-1, -1, -1):
#         list1.insert(list2[i] + 1, "(max)")
#     for i in range(len(list1)):
#         string += list1[i]
#     print(string)


# num = int(input())
# for i in range(2, num + 1):
#     if num % i == 0 and i < num:
#         print("N")
#         break
#     elif num == i:
#         print("Y")
# while True:
#     num = int(input())
#     for s1 in range (9, 12):
#         for s2 in range(9, 12):
#             for s3 in range(9, 12):
#                 for s4 in range(9, 12):
#                     for s5 in range(9, 12):
#                         for s6 in range(9, 12):
#                             for s7 in range(9, 12):
#                                 for s8 in range(9, 12):
#                                     for s9 in range(9, 12):
#                                         for s10 in range(9, 12):
#                                             if s1*1 + s2*3 + s3*9 + s4*3**3+ s5*3**4 + s6*3**5+s7*3**6+s8*3**7+s9*3**8+s10*3**9 == num:
#                                                 print("%d %d %d %d %d %d %d %d %d %d" % (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10))
#

# def func(n):
#     if n < 4:
#         return 1
#     else:
#         return func(n - 1) + func(n - 3)
#
#
# num = int(input())
# print(func(num))

# while True:
#     ipt = input()
#     if ipt == "":
#         break
#     num = ipt.split()
#     m = int(num[0])
#     n = int(num[1])
#     s1 = 1
#     s2 = 1
#     for i in range(1,  n + 1):
#         s1 *= i
#     for j in range(n):
#         s2 *= (m-j)
#     sum = int(s2 / s1)
#     print(sum)

# while True:
#     list1 = []
#     avg = 0
#     ipt = input().split()
#     for i in range(7):
#         list1.append(float(ipt[i]))
#     list1.sort()
#     for i in range(1, 6):
#         avg += list1[i] / 5
#
#     print("%s %.2f" % (ipt[7], avg))

# while True:
#     ipt = input()
#     if ipt == "":
#         break
#     num = ipt.split()
#     m = float(num[0])
#     n = float(num[1])
#     for i in range(1, 10000):
#         for j in range(0, i):
#             if n > j / i * 100 > m:
#                 print(i)
#                 break
#         else:
#             continue
#         break

# 判断是否为闰年
# def func(year):
#     if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
#         return True
#     else:
#         return False



# ipt = input().split()
# year = int(ipt[0])
# month = int(ipt[1])
# day = int(ipt[2])
# import math
# ipt = input().split()
# v = int(ipt[0])
# m = int(ipt[1])
# # print("v= %d" % v)
# # print("m= %d" % m)
# s1 = math.ceil(v / m)
# # print(s1)
# sum = 0
# count = 0
# for i in range(1, v):
#     sum += i * m
#     if sum < v:
#         count += 1
#
# print(s1 + count)


# num = int(input())
# list1 = [[0 for i in range(num)] for i in range(num)]
# for i in range(0, num):
#     list1[i] = input().split()
#
# # print(list1)
# for i in range(0, num):
#     for j in range(0, num):
#         print(list1[j][i], end=" ")
#     print()


# while True:
#     ipt = input()
#     if ipt == "":
#         break
#     list1 = list(ipt)
#     string = ""
#     for i in range(0, len(list1)):
#         if 'A' <= list1[i] <= 'Y':
#             list1[i] = chr(ord(list1[i]) + 33)
#         elif list1[i] == 'Z':
#             list1[i] = 'a'
#         elif 'a' <= list1[i] <= 'c':
#             list1[i] = '2'
#         elif 'd' <= list1[i] <= 'f':
#             list1[i] = '3'
#         elif 'g' <= list1[i] <= 'i':
#             list1[i] = '4'
#         elif 'j' <= list1[i] <= 'l':
#             list1[i] = '5'
#         elif 'm' <= list1[i] <= 'o':
#             list1[i] = '6'
#         elif 'p' <= list1[i] <= 's':
#             list1[i] = '7'
#         elif 't' <= list1[i] <= 'v':
#             list1[i] = '8'
#         elif 'w' <= list1[i] <= 'z':
#             list1[i] = '9'
#         string += list1[i]
#
#     print(string)

print("abc" in "abcd")


