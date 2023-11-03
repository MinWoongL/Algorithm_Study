# 9465_스티커_sticker
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*(N+2) for _ in range(2)]
    # print(dp)
    for i in range(2, N+2):
        dp[0][i] = sticker[0][i-2] + max(dp[0][i-2], dp[1][i-2], dp[1][i-1])
        dp[1][i] = sticker[1][i-2] + max(dp[0][i-2], dp[1][i-2], dp[0][i-1])

    print(max(dp[0][-1], dp[1][-1]))