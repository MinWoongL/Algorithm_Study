# 21317_징검다리 건너기
import sys
input = sys.stdin.readline


def bt(rock):
    for node, w in adjL[rock]:
        if node <= N and visited[node][1] >= visited[rock][1] + w:
            visited[node][1] = visited[rock][1] + w
            bt(node)
        if node <= N and visited[node][0] >= visited[rock][0] + w:
            visited[node][0] = visited[rock][0] + w
            bt(node)
    if rock + 3 <= N:
        if visited[rock + 3][0] >= visited[rock][1] + K:
            visited[rock + 3][0] = visited[rock][1] + K
            bt(rock+3)


N = int(input())

adjL = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())
    adjL[i].append([i+1, a])
    adjL[i].append([i+2, b])
K = int(input())

visited = [[5000*20]*2 for _ in range(N+1)]
visited[1][0] = 0
visited[1][1] = 0

bt(1)
print(min(visited[N]))