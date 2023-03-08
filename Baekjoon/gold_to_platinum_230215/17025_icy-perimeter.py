# 17025_icy-perimeter
from collections import deque
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())

mat = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

area_size = 0
perimeter = float('inf')

for i in range(N):
    for j in range(N):
        area = []
        if mat[i][j] == '#' and visited[i][j] == 0:
            area.append([i, j])
            q = deque()
            q.append([i, j])
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                for d in dxy:
                    nx = x + d[0]
                    ny = y + d[1]
                    if nx in range(N) and ny in range(N):
                        if mat[nx][ny] == '#' and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
                            area.append([nx, ny])
            if len(area) == area_size:
                cnt = 0
                for v in area:
                    for d2 in dxy:
                        nx = v[0]+d2[0]
                        ny = v[1]+d2[1]
                        if nx in range(N) and ny in range(N):
                            if mat[nx][ny] == '.':
                                cnt += 1
                        else:
                            cnt += 1
                if cnt <= perimeter:
                    perimeter = cnt
            elif len(area) > area_size:
                cnt = 0
                for v in area:
                    for d2 in dxy:
                        nx = v[0] + d2[0]
                        ny = v[1] + d2[1]
                        if nx in range(N) and ny in range(N):
                            if mat[nx][ny] == '.':
                                cnt += 1
                        else:
                            cnt += 1
                perimeter = cnt
                area_size = len(area)

print(area_size, perimeter)
