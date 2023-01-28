# 10989_수정렬하기 3
# N의 범위가 굉장히 큼 -> 시간복잡도, 공간복잡도를 잘 줄여야함 1<=N<=10,000,000
# 수가 중복될 수 있음, 수는 최대 10000까지만 주어짐

import sys

n = int(input())
ndi = {}
for i in range(n):
    num = int(sys.stdin.readline())
    if num not in ndi.keys():
        ndi[num] = 1
    else:
        ndi[num] += 1

ndi = sorted(ndi.items())


for v in ndi:
    for j in range(v[1]):
        print(v[0])