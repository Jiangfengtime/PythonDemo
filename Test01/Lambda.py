# lambda表达式

y = lambda x: 2 * x + 5
# 等价于:
def fun1(x):
    return 2 * x + 5
print(y(2))
print(fun1(2))

# 两个BIF函数
# filter:第一个参数是过滤的方法,第二个参数是过滤的列表
# 相当于过滤列表中为False的元素
print(list(filter(None, [1, 0, False, True])))
# 过滤奇数
print(list(filter(lambda x: x % 2, range(1, 10))))

# map:第二个参数中的每一个元素都执行一次第一个参数.并返回
print(list(map(lambda x: x * 2, range(1, 10))))



