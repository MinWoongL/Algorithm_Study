# 1010_다리놓기
import sys

def n_sum(n):
    value = 0
    nli = []
    for i in range(1,n+1):
        value += i
        nli.append(value)

    return nli


def li_sum(li):
    value = 0
    nli = []
    for v in li:
        value += v
        nli.append(value)

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
