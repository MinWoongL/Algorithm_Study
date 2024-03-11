# 2903_중앙이동알고리즘
import sys
input = sys.stdin.readline

N = int(input())

num = 2
for i in range(N):
    tmp = 2**i
    num += tmp

print(num**2)
