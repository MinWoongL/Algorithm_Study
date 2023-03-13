# 1753_최단경로_shortest-path
import sys
import heapq

V, E = map(int, input().split())

S_node = int(input())

graph = [[] for _ in range(V+1)]
dis = [float('inf')]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))

q = []
heapq.heappush(q, (0, S_node))
dis[S_node] = 0

while q:
    distance, node = heapq.heappop(q)

    if distance > dis[node]:
        continue
    else:
        for v in graph[node]:
            weight = distance + v[1]
            if weight < dis[v[0]]:
                dis[v[0]] = weight
                heapq.heappush(q, (weight, v[0]))

for i in range(1, V+1):
    if dis[i] == float('inf'):
        print('INF')
    else:
        print(dis[i])


