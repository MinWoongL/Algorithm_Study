# 1504_특정한최단경로_specific-shortest-path
import sys
import heapq
input = sys.stdin.readline


def dijkstra(s_node, e_node):
    q = []
    dis = [float('inf')] * (N + 1)
    heapq.heappush(q, (0, s_node))
    dis[s_node] = 0

    while q:
        distance, node = heapq.heappop(q)

        if distance > dis[node]:
            continue

        for v in graph[node]:
            weight = distance + v[1]
            if weight < dis[v[0]]:
                dis[v[0]] = weight
                heapq.heappush(q, (weight, v[0]))

    return dis[e_node]


N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())\

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

s_to_v1 = dijkstra(1, v1)
s_to_v2 = dijkstra(1, v2)
v1_to_v2 = dijkstra(v1, v2)
v2_to_v1 = dijkstra(v2, v1)
v1_to_N = dijkstra(v1, N)
v2_to_N = dijkstra(v2, N)

ans = min(s_to_v1 + v1_to_v2 + v2_to_N, s_to_v2 + v2_to_v1 + v1_to_N)

if ans == float('inf'):
    print(-1)
else:
    print(ans)



