# 属性访问
# class C:
#     # 定义当该类的属性被访问时的行为
#     def __getattribute__(self, item):
#         print("getattribute")
#         return super().__getattribute__(item)
#
#     # 定义当用户试图访问一个不存在的属性时的行为
#     def __getattr__(self, item):
#         print("getattr")
#
#     # 定义当一个属性被设置时的行为
#     def __setattr__(self, key, value):
#         print("setattr")
#         super().__setattr__(key, value)
#
#     # 定义一个属性被删除时的行为
#     def __delattr__(self, item):
#         print("delattr")
#         super().__delattr__(item)
#
#
# c = C()
# c.x
# c.x = 1
# del c.x


# 问题：
# class Rectangle:
#     width = 0
#     height = 0
#
#     def __init__(self, width=0, height=0):
#         self.width = width
#         self.height = height
#
#     def __setattr__(self, key, value):
#         if key == 'square':
#             self.width = value
#             self.height = value
#         else:
#             # super().__setattr__(key, value)
#             self.__dict__[key] = value
#
#     def getArea(self):
#         return self.width * self.height
#
#
# r = Rectangle(4, 5)
# print(r.getArea())
#
# r.square = 10
# print(r.getArea())


# 描述符
# class MyDecriptor:
#     def __get__(self, instance, owner):
#         print("get...", self, instance, owner)
#
#     def __set__(self, instance, value):
#         print("set...", self, instance, value)
#
#     def __delete__(self, instance):
#         print("delete...", self, instance)
#
#
# class Test:
#     x = MyDecriptor()
#
#
# test = Test()
# print(test.x)
# # get... <__main__.MyDecriptor object at 0x0000015892402DD8> <__main__.Test object at 0x000001589243F6A0> <class '__main__.Test'>
#
# print(test)     # <__main__.Test object at 0x000001C82951F6A0>
# print(Test)     # <class '__main__.Test'>
# test.x = "x-man"    # set... <__main__.MyDecriptor object at 0x0000017AA105F6D8> <__main__.Test object at 0x0000017AA105FDA0> x-man
# del test.x  # delete... <__main__.MyDecriptor object at 0x0000022D02E8F6D8> <__main__.Test object at 0x0000022D02E8FDA0>


# 编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数
# class CountList:
#     def __init__(self, *args):
#         self.values = [x for x in args]
#         self.count = {}.fromkeys(range(len(self.values)), 0)
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem__(self, item):
#         self.count[item] += 1
#         return self.values[item]

