# 28215_대피소
import sys
input = sys.stdin.readline
from itertools import combinations

N, K = map(int, input().split())

house = [list(map(int, input().split())) for _ in range(N)]

distance = [[0]*N for _ in range(N)]
for i in range(N):
    tmp = house[i]
    for j in range(N):
        if i != j:
            tmp2 = house[j]
            distance[i][j] = abs(tmp[0] - tmp2[0]) + abs(tmp[1] - tmp2[1])

c_lst = [i for i in range(N)]
comb = combinations(c_lst, K)
ans = float('inf')

for c in comb:
    min_dis = [float('inf') for _ in range(N)]
    for v in c:
        tmp = distance[v]
        for i in range(N):
            min_dis[i] = min(min_dis[i], tmp[i])
    tmp_ans = max(min_dis)

    if tmp_ans < ans:
        ans = tmp_ans

print(ans)