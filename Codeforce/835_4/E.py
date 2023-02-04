# E_Binary Inversions
import sys
import copy

T = int(input())

for tc in range(T):
    n = int(input())
    nli = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    cnt2 = 0
    if len(nli) == 1:
        print(0)
    else:
        nli_one = copy.copy(nli)
        nli_zero = copy.copy(nli)
        nli.clear()
        while cnt == 0:
            for i in range(len(nli_one)):
                if nli_one[i] == 0:
                    nli_one[i] = 1
                    cnt += 1
                    break
            break
        while cnt2 == 0:
            for j in range(len(nli_zero) - 1, -1, -1):
                if nli_zero[j] == 1:
                    nli_zero[j] = 0
                    cnt2 += 1
                    break
            break

        ans1 = 0
        ans2 = 0
        for i in range(len(nli_one)):
            if nli_one[i] == 1:
                for j in range(i, len(nli_one)):
                    if nli_one[j] == 0:
                        ans1 += 1

        for k in range(len(nli_zero)):
            if nli_zero[k] == 1:
                for l in range(k, len(nli_zero)):
                    if nli_zero[l] == 0:
                        ans2 += 1

        print(max(ans1, ans2))






