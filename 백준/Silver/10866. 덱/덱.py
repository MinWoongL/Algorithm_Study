# 10866_덱_Dequeue

import sys
from collections import deque

n = int(input())
cli = deque()

for i in range(n):

    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push_back':
        cli.append(command[1])
    elif command[0] == 'push_front':
        cli.appendleft((command[1]))
    elif command[0] == 'pop_front':
        if cli:
            print(cli.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if cli:
            print(cli.pop())
        else:
            print(-1)
    elif command[0] == 'front':
        if cli:
            print(cli[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if cli:
            print(cli[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(cli))
    else:
        if cli:
            print(0)
        else:
            print(1)


