# 2559_수열_sequence
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

n_lst = list(map(int, input().split()))
prefix = [0]
for i in range(N):
    prefix.append(prefix[-1] + n_lst[i])

# print(prefix)
ans = -1*float('inf')
for i in range(K, N+1):
    tmp = prefix[i] - prefix[i-K]
    if tmp > ans:
        ans = tmp

print(ans)