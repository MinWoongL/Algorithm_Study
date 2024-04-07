# 13334_철로_railroal
import sys
import heapq
input = sys.stdin.readline

N = int(input())

home_office = []

for _ in range(N):
    h, o = map(int, input().split())
    home_office.append(sorted([h, o]))

d = int(input())

home_office.sort(key=lambda x: x[1])
ans = 0
check = []
cnt = 0
for i in range(N):
    h, o = home_office[i]
    if o - h > d:
        continue
    while check:
        s, e = heapq.heappop(check)
        cnt -= 1
        if s >= (o - d):
            heapq.heappush(check, [s, e])
            cnt += 1
            break
    heapq.heappush(check, [h, o])
    cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)