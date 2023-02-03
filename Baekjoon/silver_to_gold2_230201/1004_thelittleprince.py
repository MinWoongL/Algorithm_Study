# 1004_어린왕자_ThelittlePrince

# 문제의 핵심은 시작점과 도착점이 몇 개의 원 안에 들어가 있는지를 셀 때, 한 쪽이 들어가 있다면 반대쪽은 바깥쪽에 있을때만 카운트를 해주는 것
import sys
import math


def distance(x, y, x2, y2):
    ans = math.sqrt((x-x2)**2 + (y-y2)**2)

    return ans


T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    n = int(input())
    planet_li = []
    for i in range(n):
        planet_li.append(list(map(int, sys.stdin.readline().split())))
    # print(planet_li)

    cnt = 0
    for i in range(len(planet_li)):
        if distance(x1, y1, planet_li[i][0], planet_li[i][1]) < planet_li[i][2]:
            if distance(x2, y2, planet_li[i][0], planet_li[i][1]) > planet_li[i][2]:
                cnt += 1
        if distance(x2, y2, planet_li[i][0], planet_li[i][1]) < planet_li[i][2]:
            if distance(x1, y1, planet_li[i][0], planet_li[i][1]) > planet_li[i][2]:
                cnt += 1
    print(cnt)


