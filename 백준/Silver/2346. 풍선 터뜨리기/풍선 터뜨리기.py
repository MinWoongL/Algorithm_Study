# 2346_풍선터뜨리기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
b_lst = list(map(int, input().split()))

q = deque()
ans = []
for i in range(N):
    q.append([b_lst[i], i])

while True:
    num, idx = q.popleft()

    ans.append(idx+1)
    if not q:
        break

    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)

print(*ans)

