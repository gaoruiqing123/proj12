# 3. 将一个列表的数据复制到另一个列表中，并反向排序输出。（40分）

num = [9,8,3,4,5,7,2,1,6,5,7,2,9,7,5,4]

num1 = []

num1=num.copy()

print("输出原来:",num)
#排序反转
num1.sort()
num1.reverse()
print("排序反转后:",num1)