# 2252_줄세우기_lining-up
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
adjL = [[] for i in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    s, g = map(int, input().split())
    adjL[s].append(g)
    indegree[g] += 1

q = deque()
ans = []
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        ans.append(i)

while q:
    now = q.popleft()

    for node in adjL[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
            ans.append(node)

print(*ans)

