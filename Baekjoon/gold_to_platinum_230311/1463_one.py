# 1463_1로만들기_one
import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*(N+3)
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i//3])+1
    if i % 2 == 0:  # 3,2 둘 다 경우의 수 해봐야함
        dp[i] = min(dp[i-1], dp[i//2])+1
    if not i % 3 and not i % 2:  # 이걸 안하면 왜 안 걸러지는지 확인해보기 ex 572
        dp[i] = min(dp[i-1], dp[i//2], dp[i//3])+1

print(dp[N])
