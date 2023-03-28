# 1405_미친로봇_crazyrobot
import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(now, cnt):
    global mat
    global ans
    x, y, p = now[0], now[1], now[2]
    if cnt == n:
        ans += now[2]
        return
    for i in range(4):
        nx = x + dxy[i][0]
        ny = y + dxy[i][1]

        if mat[nx][ny] == 0:
            mat[nx][ny] = 1
            now_p = p * prob[i]
            new = [nx, ny, now_p]
            dfs(new, cnt+1)
            mat[nx][ny] = 0


n, E, W, S, N = map(int, input().split())

prob = [E/100, W/100, S/100, N/100]
mat = [[0]*(2*n+1) for _ in range(2*n+1)]
ans = 0

start = [(2*n+1)//2, (2*n+1)//2, 1]
mat[(2*n+1)//2][(2*n+1)//2] = 1
dfs(start, 0)
print(ans)
