# 24482_깊이우선탐색_dfs4
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def dfs(graph, v, cnt):
    global ans_li
    ans_li[v] = cnt

    for i in graph[v]:
        if ans_li[i] == -1:
            dfs(graph, i, cnt+1)


N, M, R = map(int, input().split())

adjL = [[] for _ in range(N+1)]
ans_li = [-1]*(N+1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    adjL[n1].append(n2)
    adjL[n2].append(n1)
for i in range(N+1):
    adjL[i].sort(reverse=True)

dfs(adjL, R, 0)

for i in range(1, N+1):
    print(ans_li[i])