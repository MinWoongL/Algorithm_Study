# 18881_Social Distancing 2
import sys
input = sys.stdin.readline

N = int(input())
cows = []
for _ in range(N):
    x, s = map(int, input().split())
    cows.append([x, s])

cows.sort()
minimum_dis = float('inf')
for i in range(N-1):
    if cows[i][1] != cows[i+1][1]:
        if cows[i+1][0] - cows[i][0] - 1 < minimum_dis:
            minimum_dis = (cows[i+1][0] - cows[i][0] - 1)

if cows[0][1]:
    cnt = 1
else:
    cnt = 0

for i in range(N-1):
    if cows[i+1][1]:
        if cows[i+1][0] - cows[i][0] > minimum_dis:
            cnt += 1
# print(cows)
print(cnt)