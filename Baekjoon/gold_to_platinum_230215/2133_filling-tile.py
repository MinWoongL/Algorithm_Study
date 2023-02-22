# 2133_타일채우기_filling-tile

N = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(3)
else:
    dp = [0] * (N + 1)
    dp[2] = 3
    dp[3] = 0
    for i in range(4, N + 1):
        if i % 2 == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i - 2] * 3) + 2 + 2 * sum(dp[:i - 3])

    print(dp[-1])

