# 1948_임계경로_critical path
import sys
sys.setrecursionlimit(10**5)
from collections import deque
input = sys.stdin.readline


def bt_node(city):
    global cnt

    for node, t in re_adjL[city]:
        if visited[city] - visited[node] == t:
            cnt += 1
            if not back_visited[node]:
                back_visited[node] = 1
                bt_node(node)


N = int(input())
M = int(input())

adjL = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
visited = [0]*(N+1)

re_adjL = [[] for _ in range(N+1)]
for i in range(M):
    s, g, t = map(int, input().split())
    adjL[s].append([g, t])
    re_adjL[g].append([s, t])
    indegree[g] += 1


s, g = map(int, input().split())
ans = [0, 0]

q = deque()
q.append([s, 0])
while q:
    p, t = q.popleft()

    for c, time in adjL[p]:
        indegree[c] -= 1
        if visited[c] < t+time:
            visited[c] = t+time
        if not indegree[c]:
            q.append([c, visited[c]])

back_visited = [0]*(N+1)
cnt = 0
back_visited[g] = 1
bt_node(g)

print(visited[g])
print(cnt)