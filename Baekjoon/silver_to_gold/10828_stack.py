# 10828_스택

# 정수를 저장하는 명령어 스택
import sys

order_list = []

n = int(input())

for i in range(n):
    order = list(map(str, sys.stdin.readline().split()))

    if order[0] == 'push':
        order_list.append(order[1])
    elif order[0] == 'size':
        print(len(order_list))
    elif order[0] == 'empty':
        if len(order_list) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(order_list) == 0:
            print(-1)
        else:
            print(order_list[-1])
    else:
        if len(order_list) == 0:
            print(-1)
        else:
            print(order_list.pop())

