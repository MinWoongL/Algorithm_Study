# 1891_사분면_quadrant
import sys
input = sys.stdin.readline

d, target = map(int, input().split())
x, y = map(int, input().split())
dxy = [(-1, -1), (1, 0), (0, 0), (0, 1), (1, 1)]
lx, ly = 0, 0

for i in range(d):
    m = target % 10
    target //= 10
    dx, dy = dxy[m]
    lx += (dx << i)
    ly += (dy << i)

lx += x
ly -= y

ans = 0
for i in range(d-1, -1, -1):
    ans *= 10
    if (lx & (1 << i)) and (ly & (1 << i)):
        ans += 4
    elif not (lx & (1 << i)) and (ly & (1 << i)):
        ans += 3
    elif not (lx & (1 << i) and not (ly & (1 << i))):
        ans += 2
    else:
        ans += 1
if lx >= 2**d or ly >= 2**d or lx < 0 or ly < 0:
    print(-1)
else:
    print(ans)
