# 1697_숨바꼭질_hideandseek
import sys
from collections import deque

def bfs(n, k):
    q = deque([n])
    global visited
    while q:
        node = q.popleft()
        if node == k:
            return visited[node]
        for d in [node-1, node+1, 2*node]:
            if 0 <= d <= 100000 and visited[d] == 0:
                visited[d] = visited[node]+1
                q.append(d)


N, K = map(int, input().split())
visited = [0]*100001
print(bfs(N, K))
