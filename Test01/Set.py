# 集合
dict1 = {}
print(type(dict1))

set1 = {1, 2, 3, 4, 5}
print(type(set1))

# 集合中的数据是唯一且无序的：
set2 = {1, 2, 4, 2, 4, 5, 3}
print(set2)

# 将列表中重复的元素去掉
list1 = [1, 2, 4, 2, 4, 5, 3]
temp = []
for i in list1:
    if i not in temp:
        temp.append(i)
print(temp)
# 注意：集合中的元素没有顺序，所以最终的列表顺序不能确定
print(list(set(list1)))

# 集合中添加元素：add
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)
set1.remove(4)
print(set1)

# 不可变集合
set2 = frozenset([1, 2, 3])
# set2.add(4)




