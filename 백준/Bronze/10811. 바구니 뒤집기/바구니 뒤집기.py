import sys
input = sys.stdin.readline

N, M = map(int, input().split())

baguni = [i for i in range(1, N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    tmp = baguni[s-1:e]
    tmp.reverse()
    baguni = baguni[:s-1] + tmp + baguni[e:]

print(*baguni)