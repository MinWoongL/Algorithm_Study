# 17182_우주 탐사선_spaceship
import sys
input = sys.stdin.readline


def bt(idx, cost, visited, n):
    global ans
    if cost >= ans:
        return

    if n == N:
        if cost < ans:
            ans = cost
        return

    for i in range(N):
        if i != idx and not visited[i]:
            visited[i] = 1
            bt(i, cost + dist[idx][i], visited, n+1)
            visited[i] = 0


N, K = map(int, input().split())

costs = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

dist = [r for r in costs]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

v = [0]*N
v[K] = 1
bt(K, 0, v, 1)

print(ans)
