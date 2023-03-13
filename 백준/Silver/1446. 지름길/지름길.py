# 1446_지름길_shortcut
import sys
import heapq

N, D = map(int, input().split())

dis = [float('inf')]*(D+1)
dis[0] = 0
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for i in range(N):
    s, e, distance = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, distance))

q = []
heapq.heappush(q, (0, 0))

while q:
    d, sc = heapq.heappop(q)
    if dis[sc] < d:
        continue

    for v in graph[sc]:
        weight = d + v[1]

        if dis[v[0]] > weight:
            dis[v[0]] = weight
            heapq.heappush(q, (weight, v[0]))

print(dis[D])
