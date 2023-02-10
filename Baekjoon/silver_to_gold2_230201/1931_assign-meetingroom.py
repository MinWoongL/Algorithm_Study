# 1931_회의실배정_meetingroom
import sys

N = int(input())

nli = []
r_li = []
for i in range(N):
    nli.append(list(map(int, input().split())))
# print(nli)

nli.sort()

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
# 아래 방법으로 하면 max인덱스를 찾아서 pop해주는 과정에서 시간소모가 심하다 -> 시간초과

# for v in nli:
#     r_li.append(v[1]-v[0])
# print(r_li)

# while True:
#     for i in range(len(nli)-1):
#         if nli[i][1] > nli[i+1][0]:
#             idx = i
#             break
#     else:
#         print(len(nli))
#         break
#     l1 = nli[i+1][1] - nli[i+1][0]
#     l2 = nli[i][1] - nli[i][0]
#     if l1 >= l2:
#         nli.pop(i+1)
#     else:
#         nli.pop(i)
#     nli.pop()
#     nli.pop(r_li.index(max(r_li)))
#     r_li.pop(r_li.index(max(r_li)))

