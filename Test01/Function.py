# def sum(num1, num2):
#     """这是函数文档"""
#     return num1 + num2


# 调用函数
# print(sum(3, 5))
# print(sum("hello", "world"))
# 打印函数文档
# print(sum.__doc__)
# print(help(sum))


# 关键字参数
# def say(name, words):
#     print(name + "->" + words)
#
#
# say("小甲鱼", "让编程改变世界")
# say("让编程改变世界", "小甲鱼")
# say(words="让编程改变世界", name="小甲鱼")


# 默认参数
# def saySome(name="小甲鱼", words="让编程改变世界"):
#     print(name + "->" + words)
#
#
# saySome()
# saySome("特步", "非一般的感觉")


# 收集参数 相当于C语言中的可变参数
# def test(*params, num1, num2):
#     print("参数的长度是:", len(params))
#     print("第二个参数是:", params[1])
#
#
# test(1, 2, 3, 4, 5, 6, num1=7, num2=8)


# 局部变量和全局变量
# 函数体内如果调用全局变量,会创建一个相同变量名的变量并赋值.
# 所以在函数体内修改全局变量的值,在外部并不会产生影响[互不影响]
# def discounts(price, rate):
#     final_price = price * rate
#     # 不能直接获取全局变量
#     # print("old_price的值为:", old_price)
#
#     # 如果直接赋值,会重新创建一个同名的局部变量,并不会修改外部的值
#     # old_price = 50
#     # 如果要修改外部的值,需要在其前面加上global关键字
#     global old_price
#     old_price = 50
#     print("修改后的old_price的值为:", old_price)
#     return final_price
#
#
# old_price = float(input("请输入原价:"))
# rate = float(input("请输入折扣率:"))
# new_price = discounts(old_price, rate)
# print("修改后的old_price的值为:", old_price)
# print("打折后价格为", new_price)


# 嵌套函数
# def fun1():
#     print("fun1正在被调用")
#     # 嵌套函数只能被外部函数调用
#     def fun2():
#         print("fun2正在被调用")
#     fun2()
# fun1()


# 闭包
def fun1(x):
    def fun2(y):
        return x * y
    return fun2


i = fun1(8)
print(i)
print(i(7))
print(fun1(8)(7))

# def fun1():
#     x = 5
#     def fun2():
#         # 报错:因为fun2()中不能直接调用fun1中定义的变量
#         x *= x
#         return x
#     return fun2()

# python2中的解决方法:
def fun1():
    x = [5]
    def fun2():
        # 报错:因为fun2()中不能直接调用fun1中定义的变量
        x[0] *= x[0]
        return x[0]
    return fun2()

print(fun1())

# python3中的解决方法:
# 通过nolocal声明变量不是局部变量
def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()

print(fun1())







