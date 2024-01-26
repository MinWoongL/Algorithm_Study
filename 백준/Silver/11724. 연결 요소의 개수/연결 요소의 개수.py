# 11724_연결요소의 개수_Number of Connection-elements
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adjL = [[] for _ in range(N+1)]
for _ in range(M):
    s, g = map(int, input().split())
    adjL[s].append(g)
    adjL[g].append(s)

visited = [0]*(N+1)
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        q = [i]
        while q:
            now = q.pop()

            for node in adjL[now]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = 1
        cnt += 1

print(cnt)
