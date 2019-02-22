# 3. 将一个列表的数据复制到另一个列表中，并反向排序输出。（40分）

num = [1,3,5,6,4,7,8,9,5,4,3,5,8,7]

num1 =[]

num1 = num.copy()

print("原来:",num)
#排序,反转
num1.sort()
num1.reverse()
print("排序反转后:",num1)