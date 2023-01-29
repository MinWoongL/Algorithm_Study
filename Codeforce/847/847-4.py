# D. Matryoshkas

# 마트료시카 최대개수 구하기
# 시간초과
import sys
from collections import deque
t = int(input())

for i in range(t):
    n = sys.stdin.readline()

    nli = list(map(int, sys.stdin.readline().split()))
    nli.sort()

    count = 0
    while len(nli) != 0:
        matryoli = []
        current_num = nli[0]
        matryoli.append(current_num)

        for j in range(1, len(nli)):
            if nli[j] == current_num+1:
                current_num = nli[j]
                matryoli.append(current_num)

        for v in matryoli:
            nli.remove(v)

        count += 1
    print(count)

