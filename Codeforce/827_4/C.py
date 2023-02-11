# C_stripes
import sys

T = int(input())

for tc in range(T):
    a = input()
    mat = [list(map(str, input())) for _ in range(8)]
    ans = ''
    for i in range(8):
        if mat[0][i] == 'B':
            text = mat[0][i]
            for k in range(8):
                if mat[k][i] == text:
                    continue
                else:
                    break
            else:
                ans = text
        else:
            continue
    for j in range(8):
        if mat[j][0] == 'R':
            text = mat[j][0]
            for k in range(8):
                if mat[j][k] == text:
                    continue
                else:
                    break
            else:
                ans = text
        else:
            continue
    print(ans)


