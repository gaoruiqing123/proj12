import os
#读出图片
tu = open("1500361724365.jpg","rb")
s = tu.read()
tu.close()
with open("123.jpg", "wb") as n:
    n.write(s)






#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./a.png", "rb")
fdst = open(r"b.png", "wb")

#从打开的文件中读取该文件的一行
#一般是逐行读取
#可以使用for或者while循环读取文件中所有的行
fbuf = f.read()
fdst.write(fbuf)

#关闭打开的文件
fdst.close()
f.close()