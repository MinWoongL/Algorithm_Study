# 1926_그림1_painting1
import sys
from collections import deque
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

cnt = 0
max_value = 0

for i in range(N):
    for j in range(M):
        if field[i][j] and not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            tmp = 0
            q = deque()
            q.append([i, j])
            while q:
                x, y = q.popleft()
                tmp += 1

                for d in dxy:
                    nx = x + d[0]
                    ny = y + d[1]

                    if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                        if field[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
            if tmp > max_value:
                max_value = tmp

print(cnt)
print(max_value)