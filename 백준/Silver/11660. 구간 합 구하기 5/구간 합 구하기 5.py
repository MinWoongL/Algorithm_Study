# 11660_구간합구하기5_sum of sections5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
mat_base = [[mat[i][j] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(1, N):
        mat[i][j] = mat[i][j] + mat[i][j-1]

for i in range(N):
    for j in range(1, N):
        mat[j][i] = mat[j-1][i] + mat[j][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = mat[x2-1][y2-1] - mat[x2-1][y1-1] - mat[x1-1][y2-1] + mat[x1-1][y1-1]
    for i in range(x1-1, x2):
        ans += mat_base[i][y1-1]
    for j in range(y1-1, y2):
        ans += mat_base[x1-1][j]
    ans -= mat_base[x1-1][y1-1]

    print(ans)