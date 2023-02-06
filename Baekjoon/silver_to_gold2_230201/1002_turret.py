# 1002_터렛_turret
import math

T = int(input())

for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif math.sqrt((x1-x2)**2 + ((y1-y2)**2)) + min(r1, r2) <= max(r1, r2):
        if math.sqrt((x1-x2)**2 + ((y1-y2)**2)) + min(r1, r2) == max(r1, r2):
            print(1)
        else:
            print(0)
    elif math.sqrt((x1-x2)**2 + ((y1-y2)**2)) == r1+r2:
        print(1)
    elif math.sqrt((x1-x2)**2 + ((y1-y2)**2)) < r1+r2:
        print(2)
    else:
        print(0)

