# 2606_바이러스_virus

def dfs(graph, i):
    global visited
    visited[i] = True

    for v in graph[i]:
        if not visited[v]:
            dfs(graph, v)


N = int(input())
E = int(input())
visited = [0]*(N+1)

adjL = [[] for _ in range(N+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adjL[n1].append(n2)
    adjL[n2].append(n1)

dfs(adjL, 1)
cnt = 0
for v in visited:
    if visited[v]:
        cnt += 1
print(cnt-1)
