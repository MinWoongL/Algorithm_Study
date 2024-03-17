import sys
import heapq
input = sys.stdin.readline

N = int(input())

hq = []

for _ in range(N):
    heapq.heappush(hq, -1*int(input()))

ans = 0
cnt = 0
while hq:
    tmp = heapq.heappop(hq)
    tmp *= -1
    cnt += 1

    if tmp * cnt > ans:
        ans = tmp * cnt

print(ans)