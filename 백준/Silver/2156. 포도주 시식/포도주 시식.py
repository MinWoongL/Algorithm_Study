# 2156_포도주시식_wine-tasting
import sys

N = int(input())

dp = [0]*(N+1)

if N == 1:
    print(int(input()))
else:
    wine_li = []
    for _ in range(N):
        wine_li.append(int(input()))

    dp[1] = wine_li[0]
    dp[2] = wine_li[0]+wine_li[1]

    # 지금 잔 + 이전 잔, 지금 잔 + 전전 잔, 지금 잔 + 이전 잔
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], wine_li[i-1]+dp[i-2], wine_li[i-1]+wine_li[i-2]+dp[i-3])

    print(max(dp))
