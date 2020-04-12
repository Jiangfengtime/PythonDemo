# 构造和析构


# 1、__init__
# class Rectangle:
#     # __init__返回值只能是None
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getPer(self):
#         return (self.x + self.y) * 2
#
#     def getArea(self):
#         return self.x * self.y
#
#
# rec1 = Rectangle(4, 5)
# print(rec1.getPer())
# print(rec1.getArea())


# 2、__new__     此方法是对象实例化时第一个被调用的方法
# 解析：当继承了一个不可变类，而有需要对其进行修改时，就需要重写__new__方法
# class MyStr(str):
#     # 新建一个你需要的新new
#     def __new__(cls, string):
#         # 插入一条将传入的参数转换为大写的‘功能’
#         string = string.upper()
#         # 是在内建函数new(有功能)中添加这个新功能
#         return str.__new__(cls, string)
#
#
# c = MyStr("I love you")
# print(c)


# 3、__del__()
# 对象生成后，当对它的所有引用都取消后，会自动执行
# class C:
#     def __init__(self):
#         print("我是__init__方法，我被调用了")
#
#     def __del__(self):
#         print("我是__del__方法，我被调用了")
#
#
# c1 = C()
# print(c1)


# class New_int(int):
#     def __add__(self, other):
#         return int.__sub__(self, other)
#
#     def __sub__(self, other):
#         return int.__add__(self, other)
#
#
# a = New_int(5)
# b = New_int(4)
# print(a + b)
# print(a - b)


class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


a = Nint(5)
b = Nint(7)
# 因为a有__add__方法，所有__radd__不会被执行
print(a + b)    # 12
# 因为1没有__add__方法，所以__radd__会被执行
print(1 + a)    # 4     相当于：5 - 1


