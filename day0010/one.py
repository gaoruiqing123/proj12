
# 1. 使用while循环，实现持续的用户录入信息，将录入的信息以追加的方式保存至文件中，
# 当用户输入exit时，退出程序。（50分）

import os

f = open("user.txt", "w")

while True:
    us = input("请输入用户信息:")
    f.read(us)

    if us == 'exit':
        print("退出")
        break
