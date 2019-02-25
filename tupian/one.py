import os
#读出图片
tu = open("1500361724365.jpg","rb")
s = tu.read()
tu.close()
with open("123.jpg", "wb") as n:
    n.write(s)
