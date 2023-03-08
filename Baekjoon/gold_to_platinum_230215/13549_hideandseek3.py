# 13549_숨바꼭질3_hideandseek3
import sys
from collections import deque

def bfs(n, k):
    q = deque()
    q.append([n, 0])
    global visited

    if n > k:
        return n - k

    while q:
        node, dis = q.popleft()
        if node == k:
            return dis
        for d in [2*node, node-1, node+1]:
            if 0 <= d <= 100000 and visited[d] == -1:
                if d == 2*node:
                    visited[d] = True
                    q.append([d, dis])
                else:
                    visited[d] = True
                    q.append([d, dis + 1])


N, K = map(int, input().split())
visited = [-1]*100001
cnt = bfs(N, K)
print(cnt)
