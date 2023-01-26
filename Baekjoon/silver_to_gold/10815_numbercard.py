# 10815_숫자카드_numbercard
# 순차탐색은 가장 비효율적인 방법 -> dict를 이용하여 탐색을 빠르게 하거나 이분탐색과 같은 방법을 사용해야한다.

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