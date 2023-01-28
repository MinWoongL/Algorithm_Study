# 10989_수정렬하기 3
# N의 범위가 굉장히 큼 -> 시간복잡도, 공간복잡도를 잘 줄여야함 1<=N<=10,000,000
# 수가 중복될 수 있음, 수는 최대 10000까지만 주어짐

import sys

n = int(input())
ndi = {}  # 중복된 수를 세기 위한 딕셔너리
for i in range(n):
    num = int(sys.stdin.readline())
    if num not in ndi.keys():  # 키에 없으면 키에 넣고 1값 저장
        ndi[num] = 1
    else:  # 중복되었으면 추가
        ndi[num] += 1

ndi = sorted(ndi.items())  # 딕셔너리 오름차순 정렬


for v in ndi:
    for j in range(v[1]):
        print(v[0])