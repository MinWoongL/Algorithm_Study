# 2565_전깃줄_electric-wire

N = int(input())

wire_li = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)

# print(wire_li)
wire_li.sort(key=lambda x: x[0])

for i in range(N):
    for j in range(i):
        if wire_li[i][1] > wire_li[j][1]:
            dp[i] = max(dp[j]+1, dp[i])

print(N-(max(dp)+1))



