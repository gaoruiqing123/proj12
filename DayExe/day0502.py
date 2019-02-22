# 3. 将一个列表的数据复制到另一个列表中，并反向排序输出。（40分）

#创建一个列表
num = [1,3,5,7,9,4,2,6,8]
num1 = []
for i in range(len(num)):
    num1.append(num[i])
print("输出行新列表：",num1)
num1.sort()
print("排序后:",num1)
num1.reverse()
print("反向排序后:",num1)