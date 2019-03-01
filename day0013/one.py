# 1.首先，从a到z的26个小写字母中随机生成一个长度为15的字符串，，
# 然后从终端任意输入第二个字符串，也从a到z的26个小写字母中任意取值且可以重复取值，输出下面结果：（50分）
# （1）字符串1与字符串2中共同出现的所有字符。
# （2）从a到z均未在字符串1和字符串2中出现的字符
# （3）在字符串1出现但未在字符串2出现的字符
# （4）在字符串2出现但未在字符串1出现的字符
# 要求：做好输入内容的错误与异常处理；当输入字符串中出现非法字符时，给出合理提示信息并重新输入。



import random

str = 'zxcvbnmasdfghjklqwertyuiop'
str1 = ''

for i in range(0, 15):
    str1 += random.choice(str)


str2 = input("请随机输入任意字符串(15个):")
str2 = list(str2)
str1 = list(str1)
print("随机生成的字符串:", str1)
print("输入的字符串:", str2)
for j in range(0, 15):
    if (str1[j] == str2[j]):
        print("重复的字符串有:", str1[j])

