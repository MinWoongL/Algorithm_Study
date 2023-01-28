# 18258_큐2_Queue2
# deque : 보통 queue 는 FIFO 방식으로 이루어지지만 deque는 양방향 큐로써 append, pop 연산에 대해 우위를 가짐

import sys
from collections import deque

n = int(input())
dq = deque()


for i in range(n):
    msg = list(map(str, sys.stdin.readline().split()))

    if msg[0] == 'push':
        dq.append(msg[1])
    elif msg[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif msg[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif msg[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif msg[0] == 'size':
        print(len(dq))
    else:
        if dq:
            print(dq.popleft())  # dq를 활용하여 가장 앞쪽 값을 pop연산으로 제거할 수 있게함
        else:
            print(-1)



