# 10026_적록색약_red-green remedy
import sys
input = sys.stdin.readline
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N = int(input())

c_field = [list(input().strip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited_rg = [[0]*N for _ in range(N)]
cnt = 0
cnt_rg = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j] or not visited_rg[i][j]:
            if not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                group = [c_field[i][j]]

                while q:
                    x, y = q.popleft()

                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                            if not visited[nx][ny] and c_field[nx][ny] in group:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                cnt += 1
            if not visited_rg[i][j]:
                q = deque()
                q.append([i, j])
                visited_rg[i][j] = 1
                if c_field[i][j] == "R" or c_field[i][j] == "G":
                    group = ["R", "G"]
                else:
                    group = [c_field[i][j]]

                while q:
                    x, y = q.popleft()

                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                            if not visited_rg[nx][ny] and c_field[nx][ny] in group:
                                q.append([nx, ny])
                                visited_rg[nx][ny] = 1
                cnt_rg += 1

print(cnt, cnt_rg)