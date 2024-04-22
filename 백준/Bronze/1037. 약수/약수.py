import sys
input = sys.stdin.readline

N = int(input())

n_lst = list(map(int, input().split()))

n_lst.sort()
print(n_lst[0]*n_lst[-1])