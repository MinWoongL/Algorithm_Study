# 7562_나이트의이동
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
T = int(input())

for _ in range(T):
    N = int(input())
    x, y = map(int, input().split())
    gx, gy = map(int, input().split())

    if x == gx and y == gy:
        print(0)
        continue

    field = [[0]*N for i in range(N)]
    field[x][y] = 1
    q = deque()
    q.append([x, y, 0])
    ans = -1
    while q:
        x, y, cnt = q.popleft()

        if ans != -1:
            break

        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if nx == gx and ny == gy:
                ans = cnt+1
                break
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if not field[nx][ny]:
                    q.append([nx, ny, cnt+1])
                    field[nx][ny] = 1

    print(ans)