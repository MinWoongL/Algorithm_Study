# 1309_동물원_Zoo
import sys
input = sys.stdin.readline

N = int(input())

dp = [[0, 0] for _ in range(N)]

dp[0][0] = 1
dp[0][1] = 2

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1])%9901
    dp[i][1] = (2*dp[i-1][0] + dp[i-1][1])%9901

# print(dp)
print(sum(dp[-1])%9901)