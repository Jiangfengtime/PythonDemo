# 字典
Num = [1, 2, 3, 4, 5]
E_Num = ['one', 'two', 'three', 'four', 'five']
for i in range(len(Num)):
    print(Num[i], "的单词是:", E_Num[i])

dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(dict1[2])
dict2 = dict((('a', 97), ('b', 98), ('c', 99)))
print(dict2['a'])
print(dict2)

# #################fromkeys 初始化字典 #######################
dict3 = {}
print(dict3.fromkeys((1, 2, 3)))
# {1: None, 2: None, 3: None}

# 所有元素被赋相同的值
print(dict3.fromkeys((1, 2, 3), "Number"))
# {1: 'Number', 2: 'Number', 3: 'Number'}

# 后面的内容只会当成一个元素赋值给所有元素。因为fromkeys只有2个参数
print(dict3.fromkeys((1, 2, 3), ('one', 'two', 'three')))
# {1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}

# 并不会直接在原来的字典上修改，而是重新创建一个同名的字典
print(dict3.fromkeys((1, 2), "Num"))


dict4 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
for eachKey in dict4.keys():
    print(eachKey, "的英语单词时：", dict4[eachKey])

# 获取指定key值的value
print(dict4.get(3))
print(dict4[3])
# 区别：如果指定的下标不存在时，通过数组下标获取会报错，
# 但是通过get()获取时，得到的值为None
# print(dict4[6])
print(dict4.get(6))
# 如果有2个参数，则表示当指定的索引不存在时，自动创建并赋值
# 如果指定的参数存在时，则不修改原有的值
print(dict4.get(6, 'six'))
print(dict4.get(1, "ONE"))

# 判断索引值是否存在
print(3 in dict4)
print(7 in dict4)

# ############### 清空字典:clear() ###############
dict5 = {1: 'one', 2: 'two', 3: 'three'}
dict6 = dict5
dict5.clear()
print(dict5)    # {}
print(dict6)    # {}
# 如果直接使用赋值为"{}"的方法，则被赋值的字典不会被清空
dict5 = {1: 'one', 2: 'two', 3: 'three'}
dict6 = dict5
dict5 = {}
print(dict5)    # {}
print(dict6)    # {1: 'one', 2: 'two', 3: 'three'}


# ############### 拷贝 copy() ###############
dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict2 = dict1.copy()
dict3 = dict1
# 全拷贝的地址不同，修改后不会影响被赋值的字典
# 赋值后的地址相同，修改后会影响被赋值的字典
print(id(dict1))
print(id(dict2))
print(id(dict3))
print(dict2)    # {1: 'one', 2: 'two', 3: 'three'}
print(dict3)    # {1: 'one', 2: 'two', 3: 'three'}
dict1.clear()
print(dict2)    # {1: 'one', 2: 'two', 3: 'three'}
print(dict3)    # {}

# ############### 删除元素 ###############
dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# pop():弹出指定key的值
print(dict1.pop(1))
print(dict1)

# popitem():随机弹出一个元素
print(dict1.popitem())
print(dict1)

# 插入元素
dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict1.setdefault(4)
dict1.setdefault(5, 'five')
print(dict1)

# 修改元素
dict1.update({1: 'ONE'})
print(dict1)
