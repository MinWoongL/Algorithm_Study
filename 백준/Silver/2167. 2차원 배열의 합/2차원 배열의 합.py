# 2167_2차원배열의합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

prefix = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + array[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    ans = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]
    print(ans)