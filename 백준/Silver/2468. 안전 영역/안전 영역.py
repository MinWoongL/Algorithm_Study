# 2468_안전영역_safe area
import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for h in range(0, 101):
    visited = [[0]*N for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] > h and not visited[i][j]:
                stack = [[i, j]]
                visited[i][j] = 1
                area += 1
                while stack:
                    x, y = stack.pop()

                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]

                        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                            if not visited[nx][ny] and field[nx][ny] > h:
                                stack.append([nx, ny])
                                visited[nx][ny] = 1
    if area > ans:
        ans = area

print(ans)