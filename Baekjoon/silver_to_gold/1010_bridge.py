# 1010_다리놓기
# N(강 왼쪽에 놓인다리)의 개수가 커질 때 M(강 오른쪽에 놓인다리)과의 차이가 늘어날때마다 (N-1,M-1)에 놓을수 있는 최대 경우의 수 만큼 늘어난다.

import sys


def n_sum(n):  # n까지의 합을 구하는 함수
    value = 0
    nli = []
    for i in range(1,n+1):
        value += i
        nli.append(value)

    return nli


def li_sum(li):  # 리스트 안의 값을 모두 더하면서 새로운 리스트를 반환해주는 함수
    value = 0
    nli = []
    for v in li:
        value += v
        nli.append(value)  # 1 3 6 10 -> 1 4 10 20 각각 리스트의 해당 인덱스까지의 합으로 리스트 값이변경됨

    return nli


n = int(input())

for i in range(n):
    N, M = map(int, sys.stdin.readline().split())
    rge = M-N+1
    ans = 0
    sli = n_sum(rge)

    if N == 1:
        ans = M
        print(ans)
    else:
        for i in range(1, N-1):
            sli = li_sum(sli)

        print(sli[-1])
