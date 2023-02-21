# 2133_타일채우기_filling-tile

N = int(input())

dp = [0]*(N+1)
dp[2] = 3
for i in range(3, N+1):
    if i % 2 == 1:
        dp[i] = 0
    else:
        dp[i] = (dp[i-2]*3)+2*(i-3)

print(dp[-1])

