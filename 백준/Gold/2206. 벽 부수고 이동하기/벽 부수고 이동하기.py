# 2206_벽부수고 이동하기_BreakingWall and moving
import sys
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(x, y, arr, v):
    q = deque()
    q.append([x, y, 1, 0])
    visited[x][y][0] = 1
    while q:
        lx, ly, dis, brk = q.popleft()
        if lx == N-1 and ly == M-1:
            return dis

        for d in dxy:
            nx = lx + d[0]
            ny = ly + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if arr[nx][ny] == 1 and brk == 0:
                    v[nx][ny][1] = dis + 1
                    q.append([nx, ny, dis+1, 1])
                elif arr[nx][ny] == 0 and v[nx][ny][brk] == 0:
                    v[nx][ny][brk] = dis + 1
                    q.append([nx, ny, dis+1, brk])
    return 0


N, M = map(int, input().split())

mat = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
ans = bfs(0, 0, mat, visited)
# wall_li = []
#
# ans = 1000*1000
# for i in range(N):
#     for j in range(M):
#         if mat[i][j] == 1:
#             wall_li.append([i, j])
#
# for case in wall_li:
#     new_mat = [[mat[i][j] for j in range(M)] for i in range(N)]
#     new_mat[case[0]][case[1]] = 0
#     visited = [[0] * M for _ in range(N)]
#     res = bfs(0, 0, new_mat, visited)
#     if res != 0 and res < ans:
#         ans = res

if ans == 0:
    print(-1)
else:
    print(ans)
