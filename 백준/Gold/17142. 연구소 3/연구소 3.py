# 17142_연구소 3_laboratory 3
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())

labor = [list(map(int, input().split())) for _ in range(N)]

virus = []
v_cnt = 0
empty = 0
for i in range(N):
    for j in range(N):
        if labor[i][j] == 2:
            virus.append([i, j])
            v_cnt += 1
        elif labor[i][j] == 0:
            empty += 1

i_lst = [i for i in range(v_cnt)]

comb = combinations(i_lst, M)
ans = float('inf')
for c in comb:
    l_copy = [[labor[x][y] for y in range(N)] for x in range(N)]
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    for j in c:
        v = virus[j]
        l_copy[v[0]][v[1]] = "0"
        q.append([v[0], v[1], 0])
        visited[v[0]][v[1]] = 0
    check = 0
    tmp_max = 0
    while q:
        x, y, t = q.popleft()

        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if visited[nx][ny] == -1 and l_copy[nx][ny] == 0:
                    q.append([nx, ny, t+1])
                    visited[nx][ny] = t+1
                    check += 1
                    if t+1 > tmp_max:
                        tmp_max = t+1
                elif visited[nx][ny] == -1 and l_copy[nx][ny] == 2:
                    q.append([nx, ny, t+1])
                    visited[nx][ny] = t+1

    if check == empty:
        ans = min(ans, tmp_max)

if ans == float('inf'):
    print(-1)
else:
    print(ans)



