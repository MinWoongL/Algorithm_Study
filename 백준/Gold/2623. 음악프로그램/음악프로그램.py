# 2623_음악프로그램_music-program
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
adjL = [[] for i in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    pds_order = list(map(int, input().split()))
    for i in range(1, pds_order[0]):
        a = pds_order[i]
        b = pds_order[i+1]
        adjL[a].append(b)
        indegree[b] += 1

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

if len(ans) == N:
    for v in ans:
        print(v)
else:
    print(0)

