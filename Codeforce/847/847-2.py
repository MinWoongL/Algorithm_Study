# B. Taisia and Dice
import sys

t = int(input())
# n s r : 주사위 수, 모든주사위의합, 가장큰값을 제외한 주사위의 합
for i in range(t):
    n, s, r = map(int, sys.stdin.readline().split())

    ans = []
    maxn = s-r

    for i in range(n-1):
        ans.append(1)
    ans.append(maxn)

    for j in range(len(ans)-1):
        for k in range(maxn-1):
            if sum(ans) < s:
                ans[j] += 1

    for v in ans:
        print(v, end=' ')
    print('')

