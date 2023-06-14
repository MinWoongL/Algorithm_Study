# 1406_에디터_Editor
# insert, remove는 시간초과
import sys
from collections import deque
input = sys.stdin.readline

alpha1 = list(input().rstrip())
alpha2 = deque()

M = int(input())
# idx = len(alpha1)

for _ in range(M):
    order, *new = input().split()
    if order == 'P':
        alpha1.append(new[0])
    elif order == 'L':
        if alpha1:
            alpha2.appendleft(alpha1.pop())
    elif order == 'D':
        if alpha2:
            alpha1.append(alpha2.popleft())
    else:
        if alpha1:
            alpha1.pop()
print(*alpha1, sep='', end='')
print(*alpha2, sep='')