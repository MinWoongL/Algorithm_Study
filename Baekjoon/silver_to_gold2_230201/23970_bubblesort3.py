# 23970_알고리즘 수업 - 버블 정렬3_bubblesort3

# python3 로 하면 시간초과남
# list가 같은지를 매번 체크할 필요가 없음 -> 그 부분에서 시간을 절약해야함
import sys


def b_sort(li, li2, N):
    if li == li2:
        return print(1)
    else:
        for i in range(N-1, 0, -1):
            for j in range(0, i):
                if li[j] > li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]
                    if li[j] == li2[j] and li[j+1] == li2[j+1]:
                        if li == li2:
                            return print(1)
                        else:
                            pass
                    # ans = (li[j], li[j+1])
        return print(0)


n = int(input())

nli = list(map(int, sys.stdin.readline().split()))
nli2 = list(map(int, sys.stdin.readline().split()))
# print(nli)

b_sort(nli, nli2, n)

