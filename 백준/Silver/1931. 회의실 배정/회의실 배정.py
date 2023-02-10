# 1931_회의실배정_meetingroom
import sys

N = int(input())

nli = []
r_li = []
for i in range(N):
    nli.append(list(map(int, input().split())))
# print(nli)

nli.sort()
# for v in nli:
#     r_li.append(v[1]-v[0])
# print(r_li)
idx = 0
while True:
    for i in range(len(nli)-1):
        if nli[i][1] > nli[i+1][0]:
            idx = i
            break
    else:
        print(len(nli))
        break
    if nli[i+1][1] >= nli[i][1]:
        nli.pop(i+1)
    else:
        nli.pop(i)

