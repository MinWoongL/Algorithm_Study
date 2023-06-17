# 1202_보석도둑_jewelry-thief
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewel = []
bag = []
ans = 0
max_value = 0
temp_value = []

for _ in range(N):
    j = list(map(int, input().split()))
    jewel.append(j)

for _ in range(K):
    bag.append(int(input()))

jewel.sort(key=lambda x: x[0])
bag.sort()

idx = 0
for i in range(K):
    while idx < N and bag[i] >= jewel[idx][0]:
        max_value = jewel[idx][1]
        heapq.heappush(temp_value, -1*max_value)
        idx += 1
    if temp_value:
        ans += -1*heapq.heappop(temp_value)

print(ans)
