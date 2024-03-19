# 1707_이분그래프_Bipartite Graph
import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    visited = [0]*(V+1)
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        u, v = map(int, input().split())
        adjL[u].append(v)
        adjL[v].append(u)

    ans = "YES"
    for i in range(1, V + 1):
        if visited[i] == 0:
            q = deque([i])
            visited[i] = 1

            while q:
                now = q.popleft()

                for node in adjL[now]:
                    if visited[node] == 0:
                        visited[node] = 3 - visited[now]
                        q.append(node)
                    elif visited[node] == visited[now]:
                        ans = "NO"
                        break
                if ans == "NO":
                    break
        if ans == "NO":
            break

    print(ans)