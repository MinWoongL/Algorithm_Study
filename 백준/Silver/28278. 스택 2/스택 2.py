import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    num, *o = map(int, input().split())
    if num == 1:
        stack.append(o[0])
    elif num == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif num == 3:
        print(len(stack))
    elif num == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)