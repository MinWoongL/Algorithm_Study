# 미로(bfs)_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]
    x, y = 0, 0
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                x = i
                y = j
                break
    q = [(x, y, 0)]
    ans = 0
    while q:
        lx, ly, distance = q.pop(0)
        if mat[lx][ly] == 3:
            ans = distance
            break
        for d in dxy:
            nx, ny = lx + d[0], ly + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if mat[nx][ny] == 0 or mat[nx][ny] == 3:
                    q.append((nx, ny, distance+1))
        if q:
            mat[lx][ly] = 1
        else:
            break
    if ans == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {1}')
