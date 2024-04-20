# 1600_말이되고픈원숭이_Monkey wanna be horse
import sys
from collections import deque
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]
dxy_h = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

K = int(input())

W, H = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(H)]
visited = [[[40001]*(K+1) for _ in range(W)] for _ in range(H)]
# print(visited)

q = deque()
q.append([0, 0, 0, 0])
visited[0][0][0] = 0
ans = -1
while q:
    x, y, cnt, horse = q.popleft()

    if x == H-1 and y == W-1:
        ans = cnt
        break

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= H-1 and 0 <= ny <= W-1:
            if field[nx][ny] == 0 and visited[nx][ny][horse] > cnt+1:
                visited[nx][ny][horse] = cnt+1
                q.append([nx, ny, cnt+1, horse])

    if horse < K:
        for d in dxy_h:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx <= H-1 and 0 <= ny <= W-1:
                if field[nx][ny] == 0 and visited[nx][ny][horse+1] > cnt+1:
                    visited[nx][ny][horse+1] = cnt+1
                    q.append([nx, ny, cnt+1, horse+1])

print(ans)