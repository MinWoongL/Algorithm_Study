# 18870_좌표압축_coordinate-sorting

n = int(input())

coordi_li = list(map(int, input().split()))

s_li = sorted(coordi_li)
# print(s_li)
coordi_di = {}
count = 0
for v in s_li:
    if v not in coordi_di.keys():
        coordi_di[v] = count
        count += 1
# print(coordi_di)

for v in coordi_li:
    print(coordi_di[v], end=' ')