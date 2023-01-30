from collections import deque
import sys

T = int(input())

for i in range(T):
    order_li = str(sys.stdin.readline().strip())
    n = int(input())
    nli = sys.stdin.readline().strip('[]\n' + '').split(',')

    ndq = deque(nli)
    # print(ndq)

    check = 0

    if n == 0:
        ndq = []

    for j in order_li:
        if j == 'R':
            check += 1
        elif j == 'D':
            if len(ndq) == 0:
                print('error')
                break
            else:
                if check % 2 == 0:
                    ndq.popleft()
                else:
                    ndq.pop()
    else:
        if check % 2 == 0:
            print("["+",".join(ndq)+"]")
        else:
            ndq.reverse()
            print("["+",".join(ndq) + "]")