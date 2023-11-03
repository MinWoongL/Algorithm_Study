# 15654_N과M4_N-and-M 5
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int, input().split()))

n_lst.sort()
idx_lst = []
for i in range(N):
    idx_lst.append(i)
comb = permutations(idx_lst, M)

for c in comb:
    temp = []
    for v in c:
        temp.append(n_lst[v])

    print(*temp)
