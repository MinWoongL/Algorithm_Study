# 1219_오민식의 고민_OMS's worries
import sys
input = sys.stdin.readline

def Bellman_Ford(roads, p, start, goal):
    global ans
    distance[start] = p[start]

    for i in range(N):
        for j in range(N):
            for node, cost in roads[j]:
                if distance[j] != -float('inf') and distance[node] < distance[j] + p[node] - cost:
                    distance[node] = distance[j] + p[node] - cost
                    if i == N - 1:
                        if check_cycle(node, goal):
                            ans = 'Gee'
                            return

    if distance[goal] == -float('inf'):
        ans = 'gg'
    else:
        ans = distance[goal]

def check_cycle(start, goal):
    visited = [False] * N
    q = [start]
    while q:
        current = q.pop()
        if current == goal:
            return True
        visited[current] = True
        for next_node, _ in adjL[current]:
            if not visited[next_node]:
                q.append(next_node)
    return False

N, s, g, M = map(int, input().split())

adjL = [[] for _ in range(N)]
distance = [-float('inf')] * N


for _ in range(M):
    a, b, cost = map(int, input().split())
    adjL[a].append([b, cost])

profits = list(map(int, input().split()))
ans = ''

Bellman_Ford(adjL, profits, s, g)
print(ans)