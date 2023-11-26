# 1911_흙길보수하기_repairing-road
import sys
import heapq
input = sys.stdin.readline

N, L = map(int, input().split())

nulpange = []
endpoint = 0
cnt = 0
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(nulpange, [s, e])

while nulpange:
    S, E = heapq.heappop(nulpange)
    if E <= endpoint:
        continue

    if S > endpoint:
        for i in range(S, E, L):
            endpoint = i+L
            cnt += 1
    else:
        for i in range(endpoint, E, L):
            endpoint = i+L
            cnt += 1

print(cnt)





