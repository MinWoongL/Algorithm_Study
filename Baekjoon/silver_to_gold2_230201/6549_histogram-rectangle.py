# 6549_히스토그램에서 가장 큰 직사각형_histogram
from collections import deque
import sys

nli = list(map(int, sys.stdin.readline().split()))

n = nli[0]
nli = nli[1:]

print(nli)
m_rec = 0
n_stack = []

# for i in range(n):
#     while n_stack and n_stack[-1]