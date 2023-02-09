# 11047_동전0_coin0
import sys

N, K = map(int, input().split())

coin_li = []
for i in range(N):
    num = int(input())
    coin_li.append(num)

cnt = 0
value = 0
idx = -1
while True:
    if value == K:
        break
    if value + coin_li[idx] <= K:
        value += coin_li[idx]
        cnt += 1
    else:
        idx -= 1

# print(value)
print(cnt)
