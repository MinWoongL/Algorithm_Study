# 8979_올림픽_Olympics
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

q = []
for i in range(1, N+1):
    medal = list(map(int, input().split()))
    q.append(medal)

q.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

rank = 0
ans = -1
for i in range(N-1):
    if q[i][1:] == q[i+1][1:]:
        rank += 1
    if q[i][0] == K:
        ans = i+1
if ans == -1:
    ans = N

print(ans - rank)
