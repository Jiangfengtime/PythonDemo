# 类中如果属性名和方法名相同的话，属性会覆盖方法
# class C:
#     def x(self):
#         print("x-man")
#
#
# c = C()
# c.x()
# c.x = 1
# print(c.x)
# c.x()


# 绑定
# class BB:
#     def printAA():
#         print("printAA")
#
#     def printBB(self):
#         print("PrintBB")
#
#
# BB.printAA()        # 如果没有加self，则可以通过类名访问
# # BB.printBB()      # 报错
# bb = BB()
# # bb.printAA()      # 如果加了self，则不能通过类名访问
# bb.printBB()

# class CC:
#     def setXY(self, x, y):
#         self.x = x
#         self.y = y
#
#     def printXY(self):
#         print(self.x, self.y)
#
# # __dict__：获取当前对象所包含的属性
# dd = CC()
# print(dd.__dict__)
# print(CC.__dict__)
# dd.setXY(4, 5)
# print(dd.__dict__)


# 一些相关的BIF
# issubclass(class, classinfo):判断一个类是否是另一个类的子类
# 注意：
#   1、一个类被认为是其自身的子类
#   2、classinfo可以是类对象组成的元祖，只要class与其中任何
#   一个候选类的子类，则返回True
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# # 一个类被认为是其自身的子类
# print(issubclass(A, A))
# print(issubclass(B, A))


# isinstance(Object, classinfo):判断一个对象是否属于指定的类
# class A:
#     pass
#
#
# class B:
#     pass
#
#
# a = A()
# b = B()
# print(isinstance(a, A))
# print(isinstance(b, A))


# 1、hasattr(object, name):判断属性名是否属于该对象
# 2、getattr(object, name, [,default]):
#    获取对象的指定属性，如果属性不存在，则返回参数3的提示信息
# 3、setattr(object, name, value):给对象的属性赋值
# 4、delattr(object, name):删除指定属性，如果属性不存在，则抛出异常
# class C:
#     def __init__(self, x=0):
#         self.x = x
#
#
# c = C()
# # 注意：属性名需要括起来
# print(hasattr(c, 'x'))
# print(getattr(c, 'x', '你访问的属性不存在'))
# print(getattr(c, 'y', '你访问的属性不存在'))
# setattr(c, 'y', 100)
# print(getattr(c, 'y', '你访问的属性不存在'))
# delattr(c, 'y')
# print(getattr(c, 'y', '你访问的属性不存在'))


# property(fget=get, fset=set, fdel=None, doc=None)
# 第一个属性是获取属性的方法，第二个属性是设置属性的方法
# 第三个属性是删除属性的方法，第四个
class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def delSize(self, size):
        del self.size

    x = property(getSize, setSize, delSize)


# 原始的操作方法
# c = C(5)
# print(c.getSize())
# c.setSize(10)
# print(c.getSize())

# 现在的操作方法
d = C()
d.x = 10    # 相当于：d.setSize()
print(d.x)  # 相当于：d.getSize()

del d.x     # 相当于：d.delSize()
