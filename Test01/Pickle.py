import pickle
list1 = [123, 3.14, "小甲鱼", ['A', 'B', 'C']]
# 将列表中的内容写入磁盘
pickle_file = open('list1.pkl', 'wb')
# 将列表中的内容写入pickle容器
pickle.dump(list1, pickle_file)
# 关闭容器
pickle_file.close()

pickle_file = open("list1.pkl", 'rb')
list2 =pickle.load(pickle_file)
print(list2)



