# 13913_숨바꼭질4_hideandseek4
import sys
from collections import deque

def bfs(n, k):
    q = deque()
    q.append([n, 0, [n]])
    global visited
    if n > k:
        return n - k, [int(num) for num in range(n, k-1, -1)]

    while q:
        node, dis, r = q.popleft()
        if node == k:
            return dis, r
        for d in [node-1, node+1, 2*node]:
            if 0 <= d <= 100000 and visited[d] == 0:
                visited[d] = visited[node]+1
                new_r = r + [d]
                q.append([d, dis+1, new_r])


N, K = map(int, input().split())
visited = [0]*200002
cnt, road = bfs(N, K)
print(cnt)
print(*road)
