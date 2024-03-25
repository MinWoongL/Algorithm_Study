# 12904_A와B_A and B
import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

while True:
    if T == S:
        print(1)
        break

    if len(T) <= len(S):
        print(0)
        break

    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
