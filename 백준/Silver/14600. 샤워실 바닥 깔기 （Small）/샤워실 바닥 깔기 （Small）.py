# 14600_샤워실바닥깔기_flooring-shower-room
import sys

def tile_check(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            if tile[i][j]:
                return 0
    return 1


def tiling(length, x, y):
    global tile_num
    tile_num += 1
    mid = length//2

    quadrant = [[x, y], [x+mid, y], [x, y+mid], [x+mid, y+mid]]
    marking = [[x+mid-1, y+mid-1], [x+mid, y+mid-1], [x+mid-1, y+mid], [x+mid, y+mid]]

    idx = 0
    for v in quadrant:
        nx, ny = v
        mx, my = marking[idx]
        if tile_check(nx, ny, mid):
            tile[mx][my] = tile_num
        idx += 1

    if mid == 1:
        return
    tiling(mid, x, y)
    tiling(mid, x+mid, y)
    tiling(mid, x, y+mid)
    tiling(mid, x+mid, y+mid)


N = int(input())
x, y = map(int, input().split())
tile = [[0]*(2**N) for _ in range(2**N)]
tile[2**N-y][x-1] = -1

tile_num = 0
# print(tile)

tiling(2**N, 0, 0)

for row in tile:
    print(*row)
