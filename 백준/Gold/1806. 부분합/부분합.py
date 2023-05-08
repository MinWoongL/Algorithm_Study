# 1806_부분합_subsetsum
import sys
input = sys.stdin.readline

N, S = map(int, input().split())

nli = list(map(int, input().split()))

i, j = 0, 0
ans = float('inf')
s = 0
while True:
    if i > j:
        break
    if s >= S:
        ans = min(ans, j-i)
        s -= nli[i]
        i += 1
    else:
        if j < N:
            s += nli[j]
            j += 1
        else:
            break

if ans == float('inf'):
    print(0)
else:
    print(ans)