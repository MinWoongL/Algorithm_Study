# 17135_캐슬디펜스_castle-Defense
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def enemy_down(arr):
    check = 0
    for i in range(M):
        arr[N-1][i] = 0
    for i in range(N-2, -1, -1):
        for j in range(M):
            if arr[i][j] == 1:
                check += 1
                arr[i+1][j] = 1
                arr[i][j] = 0
    if check == 0:
        return 0
    else:
        return arr


dxy = [(0, -1), (-1, 0), (0, 1)]

N, M, D = map(int, input().split())

field = [[0]*M for _ in range(N+1)]
ans = 0
s_enemy = 0
for i in range(N):
    field[i] = list(map(int, input().split()))
    s_enemy += field[i].count(1)

n_li = [i for i in range(M)]
comb = combinations(n_li, 3)
for v in comb:
    if ans == s_enemy:
        break
    new_field = [[field[a][b] for b in range(M)] for a in range(N+1)]
    for i in v:
        new_field[-1][i] = 2

    cnt = 0
    while True:
        enemy = []
        for i in range(M):
            if new_field[-1][i] == 2:
                q = deque()
                q.append([N-1, i, 1])
                while q:
                    x, y, dis = q.popleft()
                    if new_field[x][y] == 1:
                        enemy.append([x, y])
                        break
                    for d in dxy:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx <= N-1 and 0 <= ny <= M-1 and dis < D:
                            q.append([nx, ny, dis + 1])
        for value in enemy:
            if new_field[value[0]][value[1]] == 1:
                new_field[value[0]][value[1]] = 0
                cnt += 1

        new_field = enemy_down(new_field)
        if new_field == 0:
            break
        if cnt == s_enemy or cnt == 3*N:
            break

    if cnt > ans:
        ans = cnt
print(ans)
