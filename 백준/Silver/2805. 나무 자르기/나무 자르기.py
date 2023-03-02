# 2805_나무자르기_cutting-tree
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_li = list(map(int, input().split()))
n_li.sort()

s = 0
e = n_li[-1]

while s <= e:
    mid = (s+e)//2
    cut_sum = 0
    for v in n_li:
        if v > mid:
            cut_sum += (v - mid)

    if cut_sum < M:
        e = mid-1
    else:
        s = mid+1

# print(s)
print(e)


