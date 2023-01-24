# 3052_나머지_remainder

li = []
for i in range(10):
    n = int(input())
    num = n%42
    if num not in li:
        li.append(num)
print(len(li))