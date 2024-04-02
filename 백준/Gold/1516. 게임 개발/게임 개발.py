# 1516_게임 개발_develop the game
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

adjL = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
times = [0]*(N+1)
builded_time = [0]*(N+1)
for i in range(1, N+1):
    t, *remain = map(int, input().split())
    indegree[i] += len(remain)-1
    times[i] = t
    for n in remain:
        if n != -1:
            adjL[n].append(i)

q = deque()

for i in range(1, N+1):
    if not indegree[i]:
        q.append(i)
        builded_time[i] = times[i]

while q:
    now = q.popleft()

    for node in adjL[now]:
        if builded_time[now] + times[node] > builded_time[node]:
            builded_time[node] = builded_time[now] + times[node]
        indegree[node] -= 1
        if not indegree[node]:
            q.append(node)

for i in range(1, N+1):
    print(builded_time[i])

