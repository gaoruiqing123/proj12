# 列表numbers中存储了一组数，numbers = [ 1, 5, -12, 37, 6,93, 100 ]，
# 将这组数按照奇数偶数分别存储到两个列表even和odd中。

numbers = [1, 5, -12, 37, 6, 93, 100]
even = []
odd = []
for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        odd.append(numbers[i])
    else:
        even.append(numbers[i])

print("偶数有:", odd)
print("奇数有:", even)