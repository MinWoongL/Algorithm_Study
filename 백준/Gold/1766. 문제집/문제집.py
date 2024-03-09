# 1766_문제집_workbook
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

adjL = [[] for _ in range(N+1)]
degree = [0]*(N+1)

for _ in range(M):
    s, g = map(int, input().split())
    adjL[s].append(g)
    degree[g] += 1

hq = []
ans = []
for i in range(1, N+1):
    if not degree[i]:
        heapq.heappush(hq, i)

while hq:
    now = heapq.heappop(hq)
    ans.append(now)

    for node in adjL[now]:
        degree[node] -= 1
        if degree[node] == 0:
            heapq.heappush(hq, node)

print(*ans)