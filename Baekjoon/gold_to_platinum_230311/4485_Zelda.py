# 4485_녹색 옷 입은 애가 젤다지_Zelda
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    global ans
    q = deque()
    q.append([x, y])

    while q:
        lx, ly = q.popleft()

        for d in dxy:
            nx, ny = lx + d[0], ly + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if visited[nx][ny] == -1 or visited[nx][ny] > (visited[lx][ly] + mat[nx][ny]):
                    visited[nx][ny] = (visited[lx][ly] + mat[nx][ny])
                    q.append([nx, ny])


tc = 1
while True:
    N = int(input())
    if N == 0:
        break

    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]

    visited[0][0] = mat[0][0]
    bfs(0, 0)
    ans = visited[-1][-1]
    print(f'Problem {tc}: {ans}')

    tc += 1
