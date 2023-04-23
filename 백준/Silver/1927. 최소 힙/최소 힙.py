# 1927_최소힙_heap
import heapq
import sys
input = sys.stdin.readline

N = int(input())

hq = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, n)