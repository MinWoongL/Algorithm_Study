# 2293_동전1_coin1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1

for i in range(N):
    tmp_coin = coins[i]
    for j in range(tmp_coin, K+1):
        if j - tmp_coin >= 0:
            dp[j] = dp[j] + dp[j - tmp_coin]

print(dp[K])
