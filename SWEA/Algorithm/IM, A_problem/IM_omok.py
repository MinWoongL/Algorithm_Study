# IM_오목판정_서울2반_이민웅

T = int(input())
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(str, input())) for _ in range(N)]

    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'o':
                for d in dxy:
                    nx = i + d[0]
                    ny = j + d[1]
                    cnt = 1
                    while 0 <= nx <= N-1 and 0 <= ny <= N-1:
                        if mat[nx][ny] == 'o':
                            cnt += 1
                            nx = nx + d[0]
                            ny = ny + d[1]
                        else:
                            break
                    if cnt == 5:
                        ans = 'YES'

    print(f'#{tc} {ans}')
