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
        if product_li[pd][0] > w:  # 현재 무게제한 인덱스값보다 넣으려는 물건의 무게가 크면 그 전 dp 값(이전 optimal value) 그대로 사용
            dp[pd][w] = dp[pd-1][w]
        else:  # 물건을 넣을수 있는경우 : 이전 optimal value를 그대로 사용(안 넣음) vs 이 전 case에서 현재 내가 넣으려는 물건 무게만큼 제외하고 물건을 넣어주는 경우
            dp[pd][w] = max(dp[pd-1][w], dp[pd-1][w-product_li[pd][0]] + product_li[pd][1])

# print(dp)
print(dp[-1][-1])
