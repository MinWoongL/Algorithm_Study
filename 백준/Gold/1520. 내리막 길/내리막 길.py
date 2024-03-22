# 1520_내리막길_downslope road
import sys
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= M-1 and 0 <= ny <= N-1:
            if field[nx][ny] < field[x][y]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


M, N = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]

ans = dfs(0, 0)
print(ans)
