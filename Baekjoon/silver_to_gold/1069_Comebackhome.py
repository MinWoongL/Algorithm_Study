# 1069_집으로 : x,y 좌표에서 0,0(집)으로 돌아오는데 걸리는 최단시간

# 문제의 핵심은 직선이 아닌 방향으로도 점프를 이용해 갔다가 되돌아오는 경우가 최단시간일수도 있다는 것을 캐치하는가
import sys
import math
x, y, d, t = map(int, sys.stdin.readline().split())

distance = math.sqrt(x*x+y*y)
n = 0
min_time = 0
n2 = 0


if d <= distance:
    while True:  # 직선거리가 아닌 방향으로 점프로 이동시에 최단시간을 재기 위해 추가
        n2 += 1
        if n2*d > distance:
            break

    while True:
        distance = distance - d
        n += 1
        if abs(distance) < d/2:
            break

    #  d만큼 집(0,0)에 도착직전까지 가고 걸어가기, d만큼 집을 넘어 한번 더 가서 걸어 되돌아오기 중 작은값, 점프로 외곽으로 돌아서 도착한 값
    min_time = min(t*n + abs(distance), t*(n+1)+abs(distance-d), float(t*n2))
else:
    #  전부걸어가기, 한번 d만큼 간 뒤 남은거리 되돌아가기 중 작은값, 2번 점프로 도착한값
    min_time = min(abs(distance), t + (d-distance), float(t*2))

print(min_time)

