import os

tu = open("1500361724365.jpg", "rb")
s = tu.read()

with open("12.jpg", "wb") as n:
    n.write(s)