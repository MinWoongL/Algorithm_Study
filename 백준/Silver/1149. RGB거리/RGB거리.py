# 1149_RGB거리_RGB-distance
import sys
input = sys.stdin.readline


N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

dp = [[0]*3 for _ in range(N)]
for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = cost[i][j] + min(dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] = cost[i][j] + min(dp[i - 1][0], dp[i - 1][2])
        else:
            dp[i][j] = cost[i][j] + min(dp[i - 1][1], dp[i - 1][0])
print(min(dp[-1]))