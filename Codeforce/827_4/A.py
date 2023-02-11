# A_Sum
import sys

T = int(input())

for tc in range(T):
    a, b, c = map(int, input().split())

    if a+b == c or b+c == a or c+a == b:
        print('YES')
    else:
        print('NO')






