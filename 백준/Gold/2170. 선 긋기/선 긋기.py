# 2170_선 긋기_draw the line
import sys
input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    x, y = map(int, input().split())
    lines.append([x, y])

lines.sort()

ans = 0
tmp_s, tmp_e = lines[0][0], lines[0][1]
for l in lines:
    s, e = l
    if s >= tmp_e:
        ans += (tmp_e-tmp_s)
        tmp_s = s
        tmp_e = e
    else:
        tmp_e = max(tmp_e, e)

ans += (tmp_e-tmp_s)
print(ans)