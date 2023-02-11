# B_Increasing
import sys

T = int(input())

for tc in range(T):
    N = int(input())
    nli = list(map(int, sys.stdin.readline().split()))
    nli.sort()
    nli_s = list(set(nli))
    if len(nli_s) == len(nli):
        print('YES')
    else:
        print('NO')

