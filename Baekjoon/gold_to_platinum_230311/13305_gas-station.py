# 13305_주유소_gas-station
import sys

N = int(input())
dis_li = list(map(int, input().split()))
cost_li = list(map(int, input().split()))

cost = cost_li[0]
ans = 0
for i in range(len(dis_li)):
    ans += dis_li[i]*cost
    if cost_li[i+1] < cost:
        cost = cost_li[i+1]

print(ans)

