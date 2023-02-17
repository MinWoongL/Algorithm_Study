# 우주선착륙2_서울2반_이민웅
T = int(input())
delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(M):
            check = 0
            landing = mat[i][j]
            for d in delta:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni <= N-1 and 0 <= nj <= M-1:
                    if mat[ni][nj] < landing:
                        check += 1
            if check >= 4:
                ans += 1

    print(f'#{tc} {ans}')