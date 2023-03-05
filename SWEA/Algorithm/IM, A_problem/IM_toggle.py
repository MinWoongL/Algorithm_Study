# 토글

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    k = 1
    while k <= M:
        if k == M or M % k == 0:
            for i in range(N):
                for j in range(N):
                    if mat[i][j] == 0:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = 0
        else:
            for i in range(N):
                for j in range(N):
                    if (i + j + 2) == k or (i + j + 2) % k == 0:
                        if mat[i][j] == 0:
                            mat[i][j] = 1
                        else:
                            mat[i][j] = 0

        k += 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                ans += 1
    print(f'#{tc} {ans}')