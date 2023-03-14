# 11779_최소비용구하기2_minimum-cost
import sys
import heapq
input = sys.stdin.readline


def dijksta(s, e):
    dis = [float('inf')] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))
    dis[s] = 0

    while q:
        distance, node = heapq.heappop(q)

        if distance > dis[node]:
            continue

        for v in graph[node]:
            weight = distance + v[1]
            if weight < dis[v[0]]:
                dis[v[0]] = weight
                visited[v[0]] = node
                heapq.heappush(q, (weight, v[0]))

    return dis[e]


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

S, E = map(int, input().split())

visited = [0]*(N+1)

ans = dijksta(S, E)
print(ans)
# print(visited)

ans_li = [E]
t = E
while t != S:
    t = visited[t]
    ans_li.append(t)

print(len(ans_li))
ans_li = ans_li[::-1]
# print(ans_li)
print(*ans_li, sep=' ')
