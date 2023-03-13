#18352_특정거리의도시찾기_specipic-distance-city
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

c_li = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    c_li[a].append(b)

q = deque()
q.append([X, 0])
visit[X] = -1
ans_li = []
while q:
    node, dis = q.popleft()
    if dis == K:
        ans_li.append(node)
    elif dis > K:
        continue
    else:
        for v in c_li[node]:
            if visit[v] == 0:
                q.append([v, dis+1])
                visit[v] = dis+1
if ans_li:
    ans_li.sort()
    print(*ans_li,sep='\n')
else:
    print(-1)
    