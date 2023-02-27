# IM_농작물수확하기_서울2반_이민웅

T = int(input())
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        ans = int(input())
    else:
        mat = [list(map(int, input())) for _ in range(N)]

        visited = [[0]*N for _ in range(N)]

        mid = N//2
        q = [(mid, mid, 0)]
        visited[mid][mid] = 1
        while q:
            x, y, dis = q.pop(0)
            for d in dxy:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                    if not visited[nx][ny]:
                        q.append((nx, ny, dis+1))
                        visited[nx][ny] = dis+1

        ans = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] <= mid:
                    ans += mat[i][j]

    print(f'#{tc} {ans}')


