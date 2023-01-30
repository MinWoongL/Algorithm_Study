# 1021_회전하는 큐_Queue6

from collections import deque
import sys

n, m = map(int, input().split())

nli = [i for i in range(1, n+1)]
ndq = deque(nli)
count = 0

# print(nli)

pick_li = list(map(int, sys.stdin.readline().split()))

for v in pick_li:
    if v == ndq[0]:
        ndq.popleft()
        # print(ndq)
    else:
        case1, case2 = 0, 0
        dq1 = deque(ndq)  # 좌측으로 이동하며 큐를 바꾸는 경우를 계산하기 위해 새로운 deque 선언
        dq2 = deque(ndq)  # 우측으로 이동하며 큐를 바꾸는 경우를 계산하기 위해 새로운 dequq 선언

        while dq1[0] != v:
            dq1.append(dq1.popleft())
            case1 += 1
        while dq2[0] != v:
            dq2.appendleft(dq2.pop())
            case2 += 1
        #  case1, case2 중 더 작은 이동을 한 경우를 count에 더해주고 ndq 값을 갱신
        if case1 < case2:
            count += case1
            while ndq[0] != v:
                ndq.append(ndq.popleft())
            ndq.popleft()
        else:
            count += case2
            while ndq[0] != v:
                ndq.appendleft(ndq.pop())
            ndq.popleft()
        # print(ndq)
print(count)