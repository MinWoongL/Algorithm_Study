# D_Coprime
import sys


def coprime(n1, n2):
    co_li = []
    for i in range(1, n2+1):
        if n1 % i == 0 and n2 % i == 0:
            co_li.append(i)
        if len(co_li) >= 2:
            break
    return co_li


T = int(input())

for tc in range(T):
    N = input()
    nli = list(map(int, input().split()))
    ans_li = []
    for i in range(1, len(nli)+1):
        for j in range(i, len(nli)+1):
            comp = coprime(nli[i-1], nli[j-1])
            if len(comp) == 1:
                ans_li.append([i, j])

    if ans_li:
        ans = 0
        for v in ans_li:
            if sum(v) > ans:
                ans = sum(v)
        print(ans)
    else:
        print(-1)




