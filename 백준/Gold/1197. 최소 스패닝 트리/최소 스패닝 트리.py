# 1197_최소 스패닝 트리_MST
import sys
input = sys.stdin.readline


def findset(node):
    while parent[node] != node:
        node = parent[node]
    return node


def union(x, y):
    parent[findset(y)] = findset(x)


V, E = map(int, input().split())

graph = []
parent = [i for i in range(V+1)]
for _ in range(E):
    s, g, w = map(int, input().split())
    graph.append([s, g, w])

graph.sort(key=lambda x: x[2])

weight = 0
cnt = 0

for e in graph:
    u, v, w = e
    if cnt == V:
        break

    if findset(u) != findset(v):
        cnt += 1
        weight += w
        union(u, v)

print(weight)
