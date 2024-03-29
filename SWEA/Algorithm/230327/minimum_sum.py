# 서울2반_minimum-sum

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]

    dp[0][0] = mat[0][0]

    for i in range(1, N):
        dp[0][i] = dp[0][i-1] + mat[0][i]
        dp[i][0] = dp[i-1][0] + mat[i][0]

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + mat[i][j]

    # print(dp[-1][-1])

    print(f'#{tc} {dp[-1][-1]}')
