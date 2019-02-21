# 2. 编写程序，生成一个包含50个随机整数的列表，
# # 随机整数的范围是从-10到10，然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表。（
# # 15分：生成随机列表5分，得出正负数新列表各5分）

#生成50个随机整数
import random
list = []
zlist = []
flist = []
for i in range(50):
    list.append(random.randint(-10,10))
    #判断正负数
    if(list[i]>0):
        zlist.append(list[i])
    elif(list[i]<0):
        flist.append(list[i])
print(list)
print("正数:",zlist)
print("负数:",flist)