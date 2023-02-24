# 홈 방범 서비스_서울2반_이민웅
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    q = [(x,y)]
    visited[x][y] = 1
    cost = K * K + (K - 1) ** 2

    if mat[x][y]:
        cnt = 1
    else:
        cnt = 0

    while q:
        lx, ly = q.pop(0)
        if visited[lx][ly] < K:
            for d in dxy:
                nx = lx + d[0]
                ny = ly + d[1]
                if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                    if visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[lx][ly] + 1
                        if mat[nx][ny]:
                            cnt += 1
    if cost <= cnt * h:
        return cnt
    else:
        return 0


T = int(input())

for tc in range(1, 1 + T):
    N, h = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    K = 1
    while K <= N + 1:
        for i in range(N):
            for j in range(N):
                value = bfs(i, j)
                if value > ans:
                    ans = value
        K += 1

    print(f'#{tc} {ans}')

