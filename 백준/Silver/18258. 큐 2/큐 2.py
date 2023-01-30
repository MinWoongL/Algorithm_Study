import sys
from collections import deque

T = int(input())
que1 = deque([])

for _ in range(T):
    rec = sys.stdin.readline().split()

    if rec[0] == 'push':
        que1.append(rec[1])
    elif rec[0] == 'pop':
        if len(que1) == 0:
            print(-1)
        else:
            print(que1.popleft())
    elif rec[0] == 'size':
        print(len(que1))
    elif rec[0] == 'empty':
        if len(que1) == 0:
            print(1)
        else:
            print(0)
    elif rec[0] == 'front':
        if len(que1) == 0:
            print(-1)        
        else:
            print(que1[0])
    elif rec[0] == 'back':
        if len(que1) == 0:
            print(-1)
        else:
            print(que1[-1])