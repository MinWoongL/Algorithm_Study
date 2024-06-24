# 1024_수열의 합
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

ans = [-1]
for i in range(L, 101):
    tmp = N - (i*(i-1))//2
    # print(tmp)
    if tmp%i == 0 and tmp >= 0:
        s = tmp // i
        ans = [k+s for k in range(i)]
        break

print(*ans)