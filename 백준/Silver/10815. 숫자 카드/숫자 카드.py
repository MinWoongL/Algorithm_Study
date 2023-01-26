# 10815_숫자카드_numbercard

import sys

sanggeun = int(input())
sgli = list(map(int, sys.stdin.readline().split()))
sgdi = {}

m = int(input())
mli = list(map(int, sys.stdin.readline().split()))

for v in sgli:
    sgdi[v] = 0

for v in mli:
    if v in sgdi.keys():
        print(1,end=' ')
    else:
        print(0,end=' ')