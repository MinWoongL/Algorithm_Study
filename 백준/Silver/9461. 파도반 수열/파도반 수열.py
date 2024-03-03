# 9461_파도반수열_wave-sequence
import sys
input = sys.stdin.readline

dp = [0]*(101)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
for i in range(5, 101):
    dp[i] = dp[i-5] + dp[i-1]

T = int(input())

for _ in range(T):
    print(dp[int(input())])