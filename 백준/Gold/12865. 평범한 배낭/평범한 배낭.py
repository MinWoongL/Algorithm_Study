# 12865_평범한 배낭_knapsack

N, W = map(int, input().split())

product_li = [[0, 0]]
for i in range(N):
    product_li.append(list(map(int, input().split())))


# print(product_li)
dp = [[0 for i in range(W+1)] for i in range(N+1)]


# for pd in range(N+1):
#     for w in range(W+1):
#         if pd == 0 and w == 0:  # 0번 물건, 무게제한 0까지는 일단 0으로 다 채움
#             dp[pd][w] = 0
#         elif product_li[pd-1][0] <= w:
#             dp[pd][w] = max(product_li[pd-1][1]+dp[pd-1][w-product_li[pd-1][0]], dp[pd-1][w])
#         else:
#             dp[pd][w] = dp[pd-1][w]

for pd in range(1, N+1):
    for w in range(1, W+1):
        if product_li[pd][0] > w:
            dp[pd][w] = dp[pd-1][w]
        else:
            dp[pd][w] = max(dp[pd-1][w], dp[pd-1][w-product_li[pd][0]] + product_li[pd][1])

# print(dp)
print(dp[-1][-1])
