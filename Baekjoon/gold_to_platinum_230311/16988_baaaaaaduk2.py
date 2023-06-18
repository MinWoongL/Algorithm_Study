# 16988_Baaaaaaaaaduk2
import sys
from itertools import combinations
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def dfs(x, y):
    global new_field
    global visited
    global temp

    space_checker = 0
    point = 1

    stack = []
    stack.append([x, y])
    visited[x][y] = 1

    while stack:
        lx, ly = stack.pop()

        for d in dxy:
            nx = lx + d[0]
            ny = ly + d[1]

            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and visited[nx][ny] == -1:
                if new_field[nx][ny] == 2:
                    stack.append([nx, ny])
                    visited[nx][ny] = 1
                    point += 1
                elif new_field[nx][ny] == 0:
                    space_checker += 1
    if space_checker == 0:
        temp += point


N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
comb = []

for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            comb.append([i, j])

ans = 0

for case in combinations(comb, 2):
    visited = [[-1]*M for _ in range(N)]
    new_field = [[field[a][b] for b in range(M)] for a in range(N)]
    temp = 0
    for v in case:
        new_field[v[0]][v[1]] = 1

    for i in range(N):
        for j in range(M):
            if new_field[i][j] == 2 and visited[i][j] == -1:
                dfs(i, j)
    if temp > ans:
        ans = temp

print(ans)