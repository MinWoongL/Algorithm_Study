# 7576_tomato
import sys
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

M, N = map(int, input().split())

tomato_mat = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
max_dis = 0
q = deque()
cnt = 0
for i in range(N):
    for j in range(M):
        if tomato_mat[i][j] == 1:
            dis = 1
            visited[i][j] = dis
            q.append((i, j, dis))
            cnt += 1
if cnt == 0:
    print(max_dis - 1)
else:
    while q:
        x, y, dis = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if tomato_mat[nx][ny] == 0:
                    if visited[nx][ny] == 0 or visited[nx][ny] > dis + 1:
                        q.append((nx, ny, dis+1))
                        visited[nx][ny] = dis+1

    check = True
    for i in range(N):
        for j in range(M):
            if tomato_mat[i][j] != -1 and visited[i][j] == 0:
                max_dis = 0
                check = False
                break
            else:
                if visited[i][j] > max_dis:
                    max_dis = visited[i][j]
        if check is False:
            break

    print(max_dis-1)
