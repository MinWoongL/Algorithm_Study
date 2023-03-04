# 15686_치킨배달_chicken-delivery
import sys
from itertools import combinations
input = sys.stdin.readline

def chicken_to_home(a, b, c, d):
    ans = abs(a - c) + abs(b - d)
    return ans


N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

chicken_li = []
home_li = []

ans = 100000
for i in range(N):
    for j in range(N):
        if mat[i][j] == 2:
            chicken_li.append([i, j])
        elif mat[i][j] == 1:
            home_li.append([i, j])
c_li = [i for i in range(0, len(chicken_li))]
chicken_comb = combinations(c_li, M)
distance = [[0]*(len(chicken_li)) for _ in range(len(home_li))]

for i in range(len(home_li)):
    for j in range(len(chicken_li)):
        x, y = chicken_li[j][0], chicken_li[j][1]
        x2, y2 = home_li[i][0], home_li[i][1]
        distance[i][j] = chicken_to_home(x, y, x2, y2)

for case in chicken_comb:
    new_mat = [[] for _ in range(len(home_li))]
    for v in case:
        idx = 0
        while idx < len(home_li):
            new_mat[idx].append(distance[idx][v-1])
            idx += 1

    check = 0
    for r in new_mat:
        check += min(r)
    if check <= ans:
        ans = check

print(ans)

