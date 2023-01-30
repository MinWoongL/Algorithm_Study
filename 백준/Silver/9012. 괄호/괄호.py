import sys
from collections import deque

T = int(input())
gual_list = deque([])

for i in range(T):
    gual = sys.stdin.readline().split()
    y = 0
    gual_list = deque([])
    for i in range(len(gual[0])):
        if gual[0][i] == '(':
            gual_list.append(1)
        elif gual[0][i] == ')':
            if len(gual_list) == 0:
                y += 1
                break
            else:
                gual_list.pop()
    
    if len(gual_list) == 0 and y == 0:
        print('YES')
    else:
        print('NO')