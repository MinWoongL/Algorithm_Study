# 1260_dfs and bfs

def dfs(graph, s):
    global visited
    global dfs_li
    visited[s] = True

    dfs_li.append(s)
    graph[s].sort()
    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i)


def bfs(graph, s):
    global visited2
    ans_li = []
    visited2[s] = 1
    q = [s]
    while q:
        node = q.pop(0)
        ans_li.append(node)
        graph[node].sort()
        for i in graph[node]:
            if visited2[i] == 0:
                q.append(i)
                visited2[i] = visited2[node]+1
    return ans_li


N, M, V = map(int, input().split())

visited = [0]*(N+1)
visited2 = [0]*(N+1)
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adjL[n1].append(n2)
    adjL[n2].append(n1)


dfs_li = []
dfs(adjL, V)
bfs_li = bfs(adjL, V)

print(*dfs_li)
print(*bfs_li)
