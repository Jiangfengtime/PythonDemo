# class Animal:
#     # 属性
#     legs = 4
#     name = 'animal'
#     shell = False
#     # 方法
#     def run(self):
#         print('动物向前爬')
#
#     def sleep(self):
#         print("动物要睡觉")
#
#
# class Turtle(Animal):
#     # 属性
#     color = 'green'
#     weight = 10
#     legs = 4
#     shell = True
#     mouth = '大嘴'
#
#     # 方法
#     def climb(self):
#         print("向前爬")
#
#     def run(self):
#         print("向前跑")
#
#     def bite(self):
#         print("咬人")
#
#     def sleep(self):
#         print("睡觉")
#
#
# tt = Turtle()
# tt.sleep()


# class MyList(list):
#     pass
#
#
# list2 = MyList()
#
# list2.append(5)
# list2.append(3)
# list2.append(4)
# list2.append(1)
# print(list2)
# list2.sort()
# print(list2)

# self
# class Ball:
#     def setName(self, name):
#         self.name = name
#
#     def kick(self):
#         print("我叫%s,该死的，谁踢我" % self.name)
#
#
# a = Ball()
# a.setName("球A")
# b = Ball()
# b.setName("球B")
# a.kick()
# b.kick()

# 魔法方法
# class Ball:
#     def __init__(self, name):
#         self.name = name
#
#     def kick(self):
#         print("我叫%s,该死的，谁踢我" % self.name)
#
#
# a = Ball("球A")
# b = Ball("球B")
# a.kick()
# b.kick()

# 私有元素
# class Person:
#     __name = "小甲鱼"
#
#     def getName(self):
#         return self.__name
#
# p = Person()
# print(p.getName())
#
# print(p._Person__name)


# 组合
# class Turtle:
#     def __init__(self, x):
#         self.num = x
#
#
# class Fish:
#     def __init__(self, x):
#         self.num = x
#
#
# class Pool:
#     def __init__(self, x, y):
#         self.turtle = Turtle(x)
#         self.fish = Fish(y)
#
#     def print_num(self):
#         print("乌龟有 %d 只，小鱼有 %d 条"
#               % (self.turtle.num, self.fish.num))
#
#
# pool = Pool(5, 7)
#
# pool.print_num()


class C:
    count = 0


a = C()
b = C()
c = C()
print(a.count)
print(b.count)
print(c.count)

c.count = 10
print(a.count)
print(b.count)
print(c.count)

C.count = 100
print(a.count)
print(b.count)
print(c.count)

