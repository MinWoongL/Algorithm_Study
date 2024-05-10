import sys
input = sys.stdin.readline

N = int(input())

n_lst = set(list(map(int, input().split())))
n_lst = list(n_lst)
n_lst.sort()
print(*n_lst)