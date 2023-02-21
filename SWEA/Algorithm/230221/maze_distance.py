# 미로의 거리_서울2반_이민웅

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
    q = [(x, y, 0)]  # 시작위치 + 시작거리
    ans = 0
    while q:
        lx, ly, distance = q.pop(0)  # 현재위치와 현재거리를 큐에서 pop
        if mat[lx][ly] == 3:
            ans = distance  # 도착점이면 거리를 정답에 저장
            break
        for d in dxy:
            nx, ny = lx + d[0], ly + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if mat[nx][ny] == 0 or mat[nx][ny] == 3:
                    q.append((nx, ny, distance+1))  # 현재위치에서 주변으로 갈 수 있으면 주변위치를 저장
                                                    # 거리는 현재위치의 거리 + 1
        if q:
            mat[lx][ly] = 1
        else:
            break
    if ans == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {ans - 1}')
