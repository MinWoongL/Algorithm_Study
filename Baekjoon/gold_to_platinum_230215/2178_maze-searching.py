# 2178_미로탐색_maze
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(x, y):
    q = [(x, y, 0)]
    visited[x][y] = 0
    while q:
        lx, ly, dis = q.pop(0)
        if lx == N-1 and ly == M-1:
            return dis
        for d in dxy:
            nx = lx + d[0]
            ny = ly + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if field[nx][ny] == 1 and visited[nx][ny] == -1:
                    q.append((nx, ny, dis+1))
                    visited[nx][ny] = dis+1


N, M = map(int, input().split())

field = [list(map(int, input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
ans = bfs(0, 0)
print(ans+1)
