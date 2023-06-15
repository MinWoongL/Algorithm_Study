# 2665_미로만들기_makeMaze
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
room = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
# print(visited)

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = deque()
q.append([0, 0, 0])
visited[0][0] = 0

while q:
    x, y, cnt = q.popleft()

    if x == N-1 and y == N-1:
        break

    for d in dxy:
        dx = x + d[0]
        dy = y + d[1]
        if 0 <= dx <= N-1 and 0 <= dy <= N-1:
            if visited[dx][dy] == -1 or visited[dx][dy] > cnt:
                if room[dx][dy] == 1:
                    q.appendleft([dx, dy, cnt])
                    visited[dx][dy] = cnt
                else:
                    q.append([dx, dy, cnt+1])
                    visited[dx][dy] = cnt+1
print(visited[-1][-1])

