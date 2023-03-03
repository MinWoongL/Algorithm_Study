# 24479_깊이우선탐색_dfs
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    graph[v].sort()

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)


N, M, R = map(int, input().split())

adjL = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for _ in range(M):
    n1, n2 = map(int, input().split())
    adjL[n1].append(n2)
    adjL[n2].append(n1)

dfs(adjL, R, visited)

for i in range(1, N+1):
    print(visited[i])
