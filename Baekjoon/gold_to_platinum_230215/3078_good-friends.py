# 3078_좋은친구_good-friends
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

dq = deque()
cnt = 0
dp = [0] * 21

for _ in range(N):
    word = input().rstrip()
    if len(dq) < K:
        dq.append(len(word))
        dp[len(word)] += 1
        cnt += (dp[len(word)]-1)
    else:
        dq.append(len(word))
        dp[len(word)] += 1
        cnt += (dp[len(word)]-1)
        tmp = dq.popleft()
        dp[tmp] -= 1
print(cnt)

