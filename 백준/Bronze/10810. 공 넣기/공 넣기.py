import sys
input = sys.stdin.readline
N, M = map(int, input().split())

bag = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())

    for n in range(i-1, j):
        bag[n] = k
print(*bag)