# 2003_수들의 합2_sum of numbers2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int, input().split()))
prefix = [0]
for i in range(N):
    prefix.append(prefix[-1] + n_lst[i])

i, j = 0, 0
cnt = 0
presum = prefix[0]
while j <= N:
    presum = prefix[j] - prefix[i]
    if presum == M:
        cnt += 1
        j += 1
    elif presum > M:
        i += 1
    else:
        j += 1

print(cnt)