# E_Scuza
import sys


T = int(input())

for tc in range(T):
    n, q = map(int, sys.stdin.readline().split())

    stair_li = list(map(int, sys.stdin.readline().split()))
    q_li = list(map(int, sys.stdin.readline().split()))
    stack = []
    ans_li = []

    for i in range(len(stair_li)):
        s_value = sum(stair_li[:i+1])
        stack.append(s_value)

    for v in q_li:
        idx = 0
        while v >= stair_li[idx] and idx < len(stair_li)-1:
            idx += 1
        if v >= stair_li[idx]:
            ans_li.append(idx)
        else:
            ans_li.append(idx-1)

    for value in ans_li:
        if value < 0:
            print(0, end=' ')
        else:
            print(stack[value], end=' ')
    print('')



