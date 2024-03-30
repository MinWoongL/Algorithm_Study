# 21758_꿀 따기_picking honeycomb
import sys
input = sys.stdin.readline

N = int(input())

honey = list(map(int, input().split()))

b1, b2 = 0, 0
comb = 0

prefix_sum = [0]
prefix_sum_re = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1]+honey[i])
    prefix_sum_re.append(prefix_sum_re[-1]+honey[N-1-i])

ans = 0
if N == 3:
    ans = 2*max(honey)

else:
    for i in range(2, N+1):
        ans = max(ans, (prefix_sum[N]-prefix_sum[1]-honey[i-1])+prefix_sum[N]-prefix_sum[i])
        ans = max(ans, (prefix_sum_re[N]-prefix_sum_re[1]-honey[N-i])+prefix_sum_re[N]-prefix_sum_re[i])

print(ans)