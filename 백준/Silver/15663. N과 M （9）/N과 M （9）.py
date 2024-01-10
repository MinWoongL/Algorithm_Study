# 15663_N과 M9
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = list(map(int, input().split()))
n_lst.sort()

numbers = [i for i in range(N)]
perm = permutations(numbers, M)
ans_check = {}
for p in perm:
    tmp = []
    checker = ''
    for v in p:
        tmp.append(n_lst[v])
        checker += (" " + str(n_lst[v]))

    if checker not in ans_check.keys():
        print(*tmp)
        ans_check[checker] = 1
    else:
        continue
