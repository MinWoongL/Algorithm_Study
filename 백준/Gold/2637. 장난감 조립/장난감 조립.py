# 2637_장난감 조립_Assemble the toy
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

adjL = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
parts = [0]*(N+1)

for i in range(M):
    x, y, k = map(int, input().split())

    indegree[x] += 1
    adjL[y].append([x, k])

q = deque()
basic = []
for i in range(1, N+1):
    if not indegree[i]:
        q.append(i)
        basic.append(i)

parts_needed = [[0]*(N+1) for _ in range(N+1)]
while q:
    now = q.popleft()
    cnt = parts[now]

    for p, need in adjL[now]:
        if sum(parts_needed[now]) == 0:
            parts_needed[p][now] += need
        else:
            for i in range(1, N+1):
                parts_needed[p][i] += parts_needed[now][i]*need
        indegree[p] -= 1
        if not indegree[p]:
            q.append(p)

for i in basic:
    print(i, parts_needed[N][i])