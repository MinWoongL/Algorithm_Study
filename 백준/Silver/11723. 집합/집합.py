# 11723_집합_Set
import sys
input = sys.stdin.readline

N = int(input())

S = set()
for _ in range(N):
    order, *num = input().split()
    if order == 'add':
        S.add(int(num[0]))
    elif order == 'remove':
        tmp = int(num[0])
        if tmp in S:
            S.remove(tmp)
    elif order == 'toggle':
        tmp = int(num[0])
        if tmp in S:
            S.remove(tmp)
        else:
            S.add(tmp)
    elif order == 'all':
        S.clear()
        for i in range(1, 21):
            S.add(i)
    elif order == 'empty':
        S.clear()
    else:
        tmp = int(num[0])
        if tmp in S:
            print(1)
        else:
            print(0)
