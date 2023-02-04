# C_Advantage
import sys

T = int(input())

for tc in range(T):
    n = int(input())
    nli = list(map(int, input().split()))

    s_nli = sorted(nli, reverse=True)

    # print(s_nli)

    for v in nli:
        if v == s_nli[0]:
            print(v - s_nli[1], end=' ')
        else:
            print(v - s_nli[0], end=' ')
    print('')
