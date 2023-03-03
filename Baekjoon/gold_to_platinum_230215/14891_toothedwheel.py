# 14891_톱니바퀴_toothedwheel
import sys
from collections import deque

t = [deque(list(map(str, input()))) for _ in range(4)]

K = int(input())

for _ in range(K):
    new_t = deque()
    for i in range(4):
        new_t.append(t[i].copy())
    # print(new_t)
    # print(new_t[0][0])
    # print(new_t[1][0])
    n, d = map(int, input().split())
    if d == 1:
        t[n-1].appendleft(t[n-1].pop())
    else:
        t[n-1].append(t[n-1].popleft())
    check1 = d
    check2 = d
    for i in range(n-1, 3):
        if new_t[i][2] != new_t[i+1][6]:
            if check1 == 1:
                t[i+1].append(t[i+1].popleft())
            else:
                t[i+1].appendleft(t[i+1].pop())
            check1 = -check1
        else:
            break

    for i in range(n-1, 0, -1):
        if new_t[i][6] != new_t[i-1][2]:
            if check2 == 1:
                t[i-1].append(t[i-1].popleft())
            else:
                t[i-1].appendleft(t[i-1].pop())
            check2 = -check2
        else:
            break
ans = 0
if t[0][0] == '1':
    ans += 1
if t[1][0] == '1':
    ans += 2
if t[2][0] == '1':
    ans += 4
if t[3][0] == '1':
    ans += 8
# print(t)
print(ans)
