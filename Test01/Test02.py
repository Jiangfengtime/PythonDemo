# # 引入随机变量模块
# import random
# # 获取1-10之间的随机整数
# rand = random.randint(1, 10)
# count = 5
# while count >= 0:
#     count -= 1
#     guess = input("请输入数字：")
#     # 游戏改进,如果输入的内容无法转换为整型时,会报错
#     # isdigit():如果输入的所有字符都是数字,则返回True
#     while not guess.isdigit():
#         guess = input("输入的类型有误,请重新输入:")
#     num = int(guess)
#     if num == rand:
#         print("恭喜你答对了")
#         break
#     elif num > rand:
#         print("抱歉,输入的值大了;")
#     else:
#         print("抱歉, 输入的值小了")
# print("游戏结束")






















