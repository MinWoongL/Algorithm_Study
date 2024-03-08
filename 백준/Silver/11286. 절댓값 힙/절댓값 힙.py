# 11286_절대값 힙_Abstract heap
import sys
import heapq
input = sys.stdin.readline

N = int(input())

hq = []

for _ in range(N):
    tmp = int(input())
    if tmp != 0:
        heapq.heappush(hq, [abs(tmp), tmp])
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
