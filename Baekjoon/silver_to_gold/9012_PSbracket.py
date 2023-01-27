# 9012_괄호_Parenthesis String_bracket

import sys


n = int(input())

for i in range(n):
    ps = list(map(str, sys.stdin.readline().strip()))
    psb = True
    while psb is True:
        if len(ps) == 0:  # 모든 괄호쌍을 제거하고 리스트가 비었다면 YES 출력
            print("YES")
            break
        elif ps[-1] == '(':  # 남은괄호쌍의 마지막이 ( 이면 NO
            print("NO")
            psb = False
            break
        else:
            for i in range(len(ps)):  # 인자가 ')'일 때, 그 전 인덱스 값이 '('이면 두 인자를 제거
                if ps[i] == ')':
                    if ps[i-1] == '(':
                        ps.pop(i-1)
                        ps.pop(i-1)
                        break
                    else:  # 남은 인자가 ')'뿐이라면 NO 출력
                        print('NO')
                        psb = False
                        break