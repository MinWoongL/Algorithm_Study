# 9205_맥주 마시면서 걸어가기_walking while drinking beer
import sys
input = sys.stdin.readline
from collections import deque
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())

for tc in range(T):
    N = int(input())

    sx, sy = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N)]
    fx, fy = map(int, input().split())

    visited = set()
    q = deque()
    q.append([sx, sy])
    visited.add((sx, sy))
    ans = "sad"

    while q:
        x, y = q.popleft()
        if abs(x-fx) + abs(y-fy) <= 1000:
            ans = "happy"
            break

        for s in stores:
            if abs(s[0]-x) + abs(s[1]-y) <= 1000 and (s[0], s[1]) not in visited:
                visited.add((s[0], s[1]))
                q.append([s[0], s[1]])

    print(ans)