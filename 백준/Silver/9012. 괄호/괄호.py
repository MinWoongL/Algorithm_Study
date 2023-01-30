# 9012_괄호_Parenthesis String_bracket

import sys

n = int(input())

for i in range(n):
    ps = list(map(str, sys.stdin.readline().strip()))
    psb = True
    while psb is True:
        if len(ps) == 0:
            print("YES")
            break
        elif ps[-1] == '(':
            print("NO")
            psb = False
            break
        else:
            for i in range(len(ps)):
                if ps[i] == ')':
                    if ps[i-1] == '(':
                        ps.pop(i-1)
                        ps.pop(i-1)
                        break
                    else:
                        print('NO')
                        psb = False
                        break