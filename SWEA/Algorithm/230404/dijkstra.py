# SWEA_최소 이동 거리
import heapq

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    dis = [float('inf')]*(V+1)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    q = []
    heapq.heappush(q, (0, 0))
    dis[0] = 0

    while q:
        distance, node = heapq.heappop(q)

        if distance > dis[node]:
            continue
        else:
            for v in graph[node]:
                w = distance + v[1]
                if w < dis[v[0]]:
                    dis[v[0]] = w
                    heapq.heappush(q, (w, v[0]))
    print(f'#{tc} {dis[V]}')

