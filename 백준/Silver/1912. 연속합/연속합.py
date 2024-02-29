# 1912_연속합_continuous sum
import sys
input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))

dp = [0]*(N)
dp[0] = n_lst[0]
tmp_sum = n_lst[0]
for i in range(1, N):
    if tmp_sum < 0:
        tmp_sum = 0
    tmp_sum += n_lst[i]
    dp[i] = max(dp[i-1], tmp_sum)

print(dp[-1])