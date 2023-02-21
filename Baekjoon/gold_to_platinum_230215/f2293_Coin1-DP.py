# 2293_동전1_Coin1-dp
# n*k 배열 계산 가능? 1<=n<=100, 1 <= k <= 10000
n, k = map(int, input().split())

coin_li = [int(input()) for _ in range(n)]
coin_li.sort()
# print(coin_li)


dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if i == 1:
            if j >= coin_li[i-1]:
                dp[i][j] = 1
        else:
            if j == coin_li[i-1]:
                dp[i][j] = dp[i-1][j] + 1
            elif j > coin_li[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin_li[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

print(dp[-1][-1])







# for col in range(coin, k+1):
#         knapsack[col] += knapsack[col - coin]
#
# print(knapsack[k])