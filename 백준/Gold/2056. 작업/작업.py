# 2056_작업_working
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

adjL = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
t_lst = [0]*(N+1)
start_time = [0]*(N+1)
for i in range(1, N+1):
    time, cnt, *works = map(int, input().split())
    t_lst[i] = time
    for w in works:
        adjL[w].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N+1):
    if not indegree[i]:
        q.append(i)
        start_time[i] = t_lst[i]

ans = 0

while q:
    now = q.popleft()

    for node in adjL[now]:
        indegree[node] -= 1
        start_time[node] = max(start_time[node], start_time[now] + t_lst[node])
        if not indegree[node]:
            q.append(node)

print(max(start_time))