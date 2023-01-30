# 5430_AC

# 출력이 str 형태인데, list(int) 형태로 출력을 제출해서 ValueError 를 받음
# reverse 함수를 매 번 활용하면, 시간초과가 난다. reverse함수의 수를 세서 pop, popleft연산을 적절히 사용해줘야함.

from collections import deque
import sys

T = int(input())

for i in range(T):
    order_li = str(sys.stdin.readline().strip())
    n = int(input())
    nli = sys.stdin.readline().strip('[]\n' + '').split(',')

    ndq = deque(nli)
    # print(ndq)

    check = 0  # reverse 함수가 나온 횟수를 체크

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
                if check % 2 == 0:  # 짝수면 popleft
                    ndq.popleft()
                else:  # 홀수면 pop
                    ndq.pop()
    else:
        if check % 2 == 0:
            print("["+",".join(ndq)+"]")
        else:
            ndq.reverse()
            print("["+",".join(ndq) + "]")




'''  ValueError
for i in range(T):
    order_li = str(sys.stdin.readline().strip())
    n = int(input())
    nli = sys.stdin.readline().strip('[]\n'+'').split(',')


    for i in range(len(order_li)):
        if '' in nli:
            if order_li[i] == 'D':
                print('error')
                break
            else:
                nli.reverse()
        else:
            if len(nli) != 0:
                if order_li[i] == 'D':
                    nli.pop(0)
                else:
                    nli.reverse()
            else:
                if order_li[i] == 'D':
                    print('error')
                    break
                else:
                    nli.reverse()
    else:
        dq = deque(nli)
        print(dq)
'''





