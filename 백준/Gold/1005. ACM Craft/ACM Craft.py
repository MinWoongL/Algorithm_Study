# 1005_ACM Craft
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    delays = [0] + list(map(int, input().split()))
    adjL = [[] for _ in range(N+1)]
    condition_cnt = [0]*(N+1)
    time_check = [0]*(N+1)
    for _ in range(K):
        s, g = map(int, input().split())
        adjL[s].append(g)
        condition_cnt[g] += 1

    goal = int(input())

    q = deque()
    for i in range(1, N+1):
        if condition_cnt[i] == 0:
            q.append(i)
            time_check[i] = delays[i]

    while q:
        now = q.popleft()

        for node in adjL[now]:
            time_check[node] = max(time_check[node], time_check[now] + delays[node])
            condition_cnt[node] -= 1
            if condition_cnt[node] == 0:
                q.append(node)

    print(time_check[goal])