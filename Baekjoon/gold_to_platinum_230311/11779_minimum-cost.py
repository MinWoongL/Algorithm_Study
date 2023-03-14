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






N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M+2):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

S, E = map(int, input().split())


