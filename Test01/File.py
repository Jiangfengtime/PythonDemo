file1 = open("C:\\Users\\Jiang锋时刻\\Desktop\\record.txt")
# print(file1.read())
# read():读取当前指针后面的指定个数字符，默认值为-1，表示读取整个文件
# 【注意是字符，而不是字节】
# print(file1.read(5))
# print(file1.read(5))

# tell():获取当前指针位置【注意：返回值是字节，而不是字符】
# print(file1.tell())

# seek(offset, from)
# from：0表示文件开始，1表示当前指针位置，2表示文件末尾
# offset表示偏移量

# print(file1.seek(45, 0))
# print(file1.readline())


# read = file1.readline()

# def split_file(filename):
#     file1 = open(filename)
#     boy = []
#     girl = []
#     count = 1
#     for each in file1:
#         if each[:6] != "======":
#             (role, speak) = each.split(':', 1)
#             if role == "小甲鱼":
#                 boy.append(speak)
#             if role == "小客服":
#                 girl.append(speak)
#         else:
#             save_file(boy, girl, count)
#             boy = []
#             girl = []
#             count += 1
#     save_file(boy, girl, count)
#     file1.close()
#
#
# def save_file(boy, girl, count):
#     file_name_boy = "boy_" + str(count) + ".txt"
#     file_name_girl = "girl_" + str(count) + ".txt"
#     boy_file = open(file_name_boy, "w")
#     girl_file = open(file_name_girl, "w")
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
#
#
# split_file("C:\\Users\\Jiang锋时刻\\Desktop\\record.txt")


file1 = open("C:\\Users\\Jiang锋时刻\\Desktop\\record.txt")
boy = []
girl = []
count = 1;
for eachline in file1.readlines():
    if eachline[:6] != "======":
        (role, spoken) = eachline.split(":", 1)
        if role == "小甲鱼":
            boy.append(spoken)
        if role == "小客服":
            girl.append(spoken)
    else:
        file_name_boy = 'boy_' + str(count) + ".txt"
        file_name_girl = 'girl_' + str(count) + ".txt"
        boy_file = open(file_name_boy, "w")
        girl_file = open(file_name_girl, "w")

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        girl = []
        boy = []
        count += 1
file_name_boy = 'boy_' + str(count) + ".txt"
file_name_girl = 'girl_' + str(count) + ".txt"
boy_file = open(file_name_boy, "w")
girl_file = open(file_name_girl, "w")

boy_file.writelines(boy)
girl_file.writelines(girl)








