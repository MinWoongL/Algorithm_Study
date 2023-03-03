# 색칠하기2

T = int(input())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, T+1):
    N = int(input())
    mat = [[0]*10 for _ in range(10)]
    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if mat[i][j] == 0:
                    mat[i][j] = c
                else:
                    mat[i][j] = 3

    # print(mat)
    ans = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 1:
                for d in dxy:
                    nx = i + d[0]
                    ny = j + d[1]
                    if 0 <= nx <= 9 and 0 <= ny <= 9:
                        if mat[nx][ny] == 1:
                            continue
                        else:
                            ans += 1
                    else:
                        ans += 1
            elif mat[i][j] == 2:
                for d in dxy:
                    nx = i + d[0]
                    ny = j + d[1]
                    if 0 <= nx <= 9 and 0 <= ny <= 9:
                        if mat[nx][ny] == 2:
                            continue
                        else:
                            ans += 1
                    else:
                        ans += 1
    print(f'#{tc} {ans}')

