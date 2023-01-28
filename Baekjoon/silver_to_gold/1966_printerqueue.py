# 1966_프린터큐_printer Queue

from collections import deque

t = int(input())

for i in range(t):
    count = 0
    n, m = map(int, input().split())
    nli = list(map(int, input().split()))
    dq = deque(nli)
    # print(nli)
    # print(dq)

    end = True
    mvalue = 0

    while end:
        for i in range(len(dq)):
            if dq[i] > mvalue:
                mvalue = dq[i]

        if dq[0] == mvalue:  # 현재 큐의 가장 앞이 중요도가 최대인 값이면 출력
            dq.popleft()
            mvalue = 0  # pop 후 mvalue 최대값 초기화
            count += 1
            if m == 0:
                print(count)
                end = False
            else:
                m -= 1
                # print(m)
        else:
            dq.append(dq.popleft())  # 중요도가 최대값이 아니면 가장 뒤로 변경
            m -= 1
            if m < 0:
                m = len(dq)-1  # len -1 값을 줘야하는 것 주의 (최대 인덱스)
            # print(m)
            # print(dq)
            # print(count)








