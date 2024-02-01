# 11659_구간합구하기4_partial-sum4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_lst = list(map(int, input().split()))

sum_lst = [0]
for i in range(N):
    sum_lst.append(sum_lst[-1]+num_lst[i])

for _ in range(M):
    s, e = map(int, input().split())
    print(sum_lst[e] - sum_lst[s-1])