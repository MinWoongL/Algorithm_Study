# 9935_문자열폭발_string-explosion
import sys

victim = str(sys.stdin.readline().strip())
boom = list(map(str, sys.stdin.readline().strip()))
boom_size = len(boom)

stack = []

if boom_size == 1:
    for s in victim:
        if s != boom[0]:
            stack.append(s)

    if stack:
        print(*stack, sep='')
    else:
        print("FRULA")
else:
    for s in victim:
        if not stack:
            stack.append(s)
        else:
            if s != boom[-1]:
                stack.append(s)
            else:
                if len(stack) >= boom_size-1:
                    if stack[-boom_size+1:] == boom[:-1]:
                        for i in range(boom_size-1):
                            stack.pop()
                    else:
                        stack.append(s)
                else:
                    stack.append(s)
    if stack:
        print(*stack, sep='')
    else:
        print('FRULA')
