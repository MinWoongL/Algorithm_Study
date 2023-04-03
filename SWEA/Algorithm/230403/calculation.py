# SWEA_연산
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    q = deque()
    q.append([N, 0])
    visited = [-1]*1000001
    visited[N] = 0
    ans = 0
    while q:
        num, dis = q.popleft()

        if num == M:
            ans = dis
            break

        for v in (num*2, num+1, num-1, num-10):
            if v <= 1000000 and visited[v] == -1:
                q.append([v, dis+1])
                visited[v] = dis+1

    print(f'#{tc} {ans}')

