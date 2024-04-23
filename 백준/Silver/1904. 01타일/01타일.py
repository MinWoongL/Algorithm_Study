# 1904_01타일_01tile
import sys
input = sys.stdin.readline

N = int(input())

# 1, (11, 00), (111, 001, 100), (1111, 1001, 1100, 0011, 0000)
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])