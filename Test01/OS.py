import os
# getcwd():返回当前工作目录
print(os.getcwd())

# chdir(path):更改当前的工作目录，如果目录不存在，则抛出异常
os.chdir("E://")
print(os.getcwd())

# listdir(path=""):获取指定目录中的文件名,如果目录不存在，则会抛出异常
print(os.listdir("E://"))

# mkdir(path):创建单层目录,如果目录已存在会抛出异常
os.mkdir("E://A/")

# makedirs(path):递归创建目录，如果目录存在则抛出异常
# os.makedirs("E://B//C")

# remove(path)：删除文件,如果文件不存在，则抛出异常
# os.remove("a.txt")

# rmdir():删除单层目录，如该目录非空则抛出异常
# os.rmdir("E://A/")

# # removedirs():递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
# os.removedirs("E://B//C")


# os.rename()



