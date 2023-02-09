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
    if value == K:  # K값과 계산값이 같아질 때 까지
        break
    if value + coin_li[idx] <= K:  # 가장 큰 금액을 더한 값이 작거나 같은경우만 +=
        value += coin_li[idx]
        cnt += 1
    else:
        idx -= 1

# print(value)
print(cnt)
