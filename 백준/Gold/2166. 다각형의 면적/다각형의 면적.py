# 2166_다각형의면적_Area-of-polygon
import sys
input = sys.stdin.readline

N = int(input())

cordi = []
for _ in range(N):
    x, y = map(int, input().split())
    cordi.append([x, y])

cordi.append(cordi[0])

xy = 0
yx = 0
for i in range(N):
    xy += cordi[i][0]*cordi[i+1][1]
    yx += cordi[i][1]*cordi[i+1][0]

ans = round(abs(xy-yx)/2, 1)

print(ans)