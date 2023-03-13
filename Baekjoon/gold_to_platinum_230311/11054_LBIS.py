# 11054_가장 긴 바이토닉부분수열_LBIS
# 97% 틀렸습니다 반례 - 2, 2 1
import sys
input = sys.stdin.readline

N = int(input())

n_li = list(map(int, input().split()))

dp = [0]*(N+1)
dp2 = [0]*(N+1)

for i in range(N):
    for j in range(i):
        if n_li[i] > n_li[j]:
            dp[i] = max(dp[j]+1, dp[i])

for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if n_li[i] > n_li[j]:
            dp2[i] = max(dp2[j]+1, dp2[i])

ans = 0
for i in range(N+1):  # 1, N+1 에서 전 범위로 수정
    if dp[i]+dp2[i] > ans:
        ans = dp[i]+dp2[i]

print(ans+1)
