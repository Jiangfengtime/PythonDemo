# 设计一个验证用户密码程序，用户只有三次机会输入错误，
# 不过如果用户输入的内容中包含"*" 则不计算在内。
# exp = input("输入用户密码：")
# count = 0
# while True:
#     password = ''
#     count += 1
#     for i in range(len(exp)):
#         if exp[i] != "*":
#             # print(exp[i])
#             password += exp[i]
#             # password = str(password)
#             # print(password)
#
#     if "123456" == password:
#         print("登录成功")
#         break
#     elif count < 3:
#         exp = input("密码错误，请重新输入：")
#
#     else:
#         print("错误次数达到3次，输入失败")
#         break


# 编写一个程序，求100~999 之间的所有水仙花数。
# for i in range(100, 999):
#     a = int(i / 100)
#     b = int((i / 10) % 10)
#     c = int(i % 10)
#     # print(a, b, c)
#     if i == (a*a*a + b*b*b + c*c*c):
#         print(i)

red = 3
yellow = 3
green = 6
for x in range(0, red + 1):
    for y in range(0, yellow + 1):
        for z in range(0, green + 1):
            if 8 == (x + y + z):
                print("有 %d 个红球，%d个黄球， %d个绿球" % (x, y ,z))







