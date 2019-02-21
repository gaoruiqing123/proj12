# 5.实现以下功能：（30分）
# 	s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python ' \
# 对这段文字中的单词进行数字统计，并且进行个数升序
# （能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）

import random
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python'

#输出原来
print("原来:",s)
#切割
s = s.split(" ")
#输出切割后
print("切割后的:",s)

#定义空字典
dic = {}
for i in s:
    key = dic.get(i)
    if(key==None):
        dic[i]=1
    else:
        dic[i]+=1
#输出字典
print("字典:",dic)
#定义空字典
dic1 = {}
#单词个数排序
sv = list(dic.values())
sv.sort()
print("值:",sv)
#去重
sv = set(sv)
sv = list(sv)
print("去重:",sv)

#排序
for i in sv:
    for j in dic:
        if(dic[j]==i):
            dic1[j]=i
print("排序后:",dic1)

