# 3009_네번째 점
import sys

rec_li = []
for i in range(3):
    rec_li.append(list(map(int, sys.stdin.readline().split())))

x = []
y = []
for v in rec_li:
    x.append(v[0])
    y.append(v[1])

ans_li =[0, 0]
for value in x:
    if x.count(value) == 1:
        ans_li[0] = value
for value in y:
    if y.count(value) == 1:
        ans_li[1] = value

print(*ans_li)
