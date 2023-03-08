# 1012_유기농배추_organic-cabbage
import sys
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(lx, ly):
    global visited
    global cabbage

    stack = [(lx, ly)]
    visited[lx][ly] = True
    while stack:
        a, b = stack.pop()
        for d in dxy:
            nx = a + d[0]
            ny = b + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if cabbage[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx, ny)


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    cabbage = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)
