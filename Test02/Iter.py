# str1 = "Hello World"
# it = iter(str1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# while True:
#     try:
#         each = next(it)
#     except StopIteration:
#         break
#     print(each)


# 生成器
# def libs():
#     a = 0
#     b = 1
#     while True:
#         a, b = b, a + b
#         yield b
#
#
# for each in libs():
#     if each > 100:
#         break
#     print(each, end=' ')
