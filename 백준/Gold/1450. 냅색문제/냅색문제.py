# 1450_냅색문제_knapsack problem
import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())

weights = list(map(int, input().split()))

a_cnt = 0
b_cnt = 0

A_lst = weights[:N//2]
B_lst = weights[N//2:]
A_new = []
B_new = []
A_dict = {}
B_dict = {}

for i in range(1, len(A_lst)+1):
    for j in combinations(A_lst, i):
        tmp = sum(j)
        if tmp <= C:
            if tmp in A_dict.keys():
                A_dict[tmp] += 1
            else:
                A_dict[tmp] = 1
                a_cnt += 1
            A_new.append(tmp)

for i in range(1, len(B_lst)+1):
    for j in combinations(B_lst, i):
        tmp = sum(j)
        if tmp <= C:
            if tmp in B_dict.keys():
                B_dict[tmp] += 1
            else:
                B_dict[tmp] = 1
                b_cnt += 1
            B_new.append(tmp)

cnt = 1

if a_cnt <= b_cnt:
    B_new.sort()
    for s in A_dict.keys():
        num = A_dict[s]
        start, end = 0, len(B_new)
        while start < end:
            mid = (start+end) // 2
            if s + B_new[mid] <= C:
                start = mid + 1
            else:
                end = mid

        cnt += (end*num)
else:
    A_new.sort()
    for s in B_dict.keys():
        num = B_dict[s]
        start, end = 0, len(A_new)
        while start < end:
            mid = (start + end) // 2
            if s + A_new[mid] <= C:
                start = mid + 1
            else:
                end = mid
        cnt += (end*num)

cnt += len(A_new)
cnt += len(B_new)
print(cnt)