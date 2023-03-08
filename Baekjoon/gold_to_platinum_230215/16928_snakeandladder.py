# 16928_뱀과사다리게임_snakeandladder
import sys
from collections import deque

N, M = map(int, input().split())

visited = [0] * 101
snake = [[] * 101]
ladder = [[] * 101]
print(visited)

for _ in range(N):
    n1, n2 = map(int, input().split())
    ladder[n1].append(n2)

for _ in range(M):
    n1, n2 = map(int, input().split())
    snake[n1].append(n2)

q = deque()
q.append([1, 0])
ans = 0
while q:
    now, cnt = q.popleft()
    if now == 100:
        ans = cnt
        break
    else:
        for i in range(1, 7):
            new = now + i
            if ladder[new] and not visited:
                q.append([ladder[new], cnt + 1])
        for i in range(1, 7):
            new = now + i
            if snake[new] and not visited:
                q.append(snake[new], cnt + 1)


