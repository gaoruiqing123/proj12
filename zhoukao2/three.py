# 3.  四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 定义变量

a = 2
b = 3
c = 4


# 判断

print("组成的三位数分别是:")
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a!=b and b!=c and c!=a):
                print("%d%d%d" % (a, b, c))