# 1932_정수삼각형
import sys
input = sys.stdin.readline

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
dp = [[tri[a][b] for b in range(len(tri[a]))] for a in range(N)]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + tri[i][0]

for i in range(1, N):
    dp[i][i] = dp[i-1][i-1] + tri[i][i]

for i in range(1, N):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1] + tri[i][j], dp[i-1][j] + tri[i][j])

print(max(dp[-1]))
