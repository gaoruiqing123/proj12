# 4.随机生成一个包含1000个字母的字符串，
# 然后统计该字符串中每个字母的数量，并输出结果（
# 要求结果以字典方式存储）（20分：随机生成字符串5分，
# 统计字母数量8分，以字典方式存储5分，输出结果2分）
import random
#定义字符串
str = 'asdfghjuyt'
str1 = ''
# 4.随机生成一个包含1000个字母的字符串，
for i in range(1000):
    str1+=random.choice(str)
#输出原来的
print("没统计之前:",str1)
#定义空字典
dic = {}
for i in str1:
    key = dic.get(i)
    #判断数量
    if(key==None):
        dic[i]=1
    else:
        dic[i]+=1
#统计之后的字典
print("统计后的:",dic)