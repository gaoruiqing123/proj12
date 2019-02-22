# 3. 将一个列表的数据复制到另一个列表中，并反向排序输出。（40分）

#创建列表

num = [1,3,5,8,9,4,6,7,3,1]
num1 = []
#拷贝
num1=num.copy()

print("原来:",num)
num1.sort()
num1.reverse()
print("拷贝反转:",num1)
