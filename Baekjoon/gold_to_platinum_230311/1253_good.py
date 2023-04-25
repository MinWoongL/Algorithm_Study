# 1253_좋다_Good
import sys
input = sys.stdin.readline

N = int(input())
n_li = list(map(int, input().split()))

n_di = {}
ans = 0
for v in n_li:
    if v in n_di.keys():
        n_di[v] += 1
    else:
        n_di[v] = 1

for i in range(N):
    for j in range(i+1, N):
        good = n_li[i] + n_li[j]
        zeros = 0
        if n_li[i] == 0:
            zeros += 1
        if n_li[j] == 0:
            zeros += 1

        if good in n_di.keys():
            if zeros == 2:
                if n_di[good] > 2:
                    ans += n_di[good]
                    n_di[good] = 0
            elif zeros == 1:
                if n_di[good] > 1:
                    ans += n_di[good]
                    n_di[good] = 0
            else:
                if n_di[good] > 0:
                    ans += n_di[good]
                    n_di[good] = 0

print(ans)