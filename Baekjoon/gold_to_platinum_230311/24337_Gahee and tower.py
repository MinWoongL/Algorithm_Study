# 24337_가희와 탑_Gahee and tower
import sys
from collections import deque
input = sys.stdin.readline

N, a, b = map(int, input().split())
ans = deque()
if a >= b:
    for i in range(1, a+1):
        ans.append(i)
    if (N-a) >= b:
        temp = ans.popleft()
        for k in range(N-b-a+1):
            ans.appendleft(1)
        ans.appendleft(temp)
    for j in range(b-1, 0, -1):
        ans.append(j)
else:
    for i in range(b, 0, -1):
        ans.append(i)
    for j in range(a-1, 0, -1):
        ans.appendleft(j)
    if (N-a-b) >= 0:
        temp = ans.popleft()
        for k in range(N-b-a+1):
            ans.appendleft(1)
        ans.appendleft(temp)

if len(ans) > N:
    print(-1)
else:
    print(*ans)