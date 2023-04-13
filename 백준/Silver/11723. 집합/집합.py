# 11723_집합_set
import sys
input = sys.stdin.readline

M = int(input())

all = set()
ans = set()

for i in range(1, 21):
    all.add(i)

for i in range(M):
    w = list(map(str, input().split()))

    cal = w[0]
    num = 0
    if cal != 'all' and cal != 'empty':
        num = int(w[1])

    if cal == 'add':
        ans.add(num)
    elif cal == 'remove':
        if num in ans:
            ans.remove(num)
    elif cal == 'toggle':
        if num in ans:
            ans.remove(num)
        else:
            ans.add(num)
    elif cal == 'all':
        ans = all
    elif cal == 'empty':
        ans.clear()
    else:
        if num in ans:
            print(1)
        else:
            print(0)
