# 14501_퇴사_resignation
import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*(N+1)

counsel_li = []
for _ in range(N):
    d, v = map(int, input().split())
    counsel_li.append([d, v])

for i in range(N-1, -1, -1):
    if counsel_li[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + counsel_li[i][0]] + counsel_li[i][1])

print(max(dp))


