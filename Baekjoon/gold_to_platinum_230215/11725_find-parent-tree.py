# 11725_트리의부모찾기_find-parent-tree

N = int(input())

adjL = [[] for _ in range(N+1)]
parent = [0]*(N+1)
visited = [0]*(N+1)
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adjL[n1].append(n2)
    adjL[n2].append(n1)

stack = [1]

while stack:
    node = stack.pop()
    visited[node] = 1
    for c in adjL[node]:
        if not visited[c]:
            stack.append(c)
            parent[c] = node
            visited[c] = 1

for i in range(2, N+1):
    print(parent[i])

