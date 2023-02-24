# 14503_로봇청소기_robotCleaner
import sys

input = sys.stdin.readline
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

dxy2 = {0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
        }

N, M = map(int, input().split())

r, c, di = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

dq = [(r, c, di)]
ans = 0
while dq:
    x, y, direction = dq.pop()
    if room[x][y] == 0:
        room[x][y] = 2
        ans += 1

    room_check = False

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
            if room[nx][ny] == 0:
                room_check = True
    if room_check:
        while True:
            direction -= 1
            if direction == -1:
                direction = 3
            nx2 = x + dxy2[direction][0]
            ny2 = y + dxy2[direction][1]

            if room[nx2][ny2] == 0:
                dq.append([nx2, ny2, direction])
                break
    else:
        back = direction - 2
        if back == -1:
            back = 3
        elif back == -2:
            back = 2
        nx3 = x + dxy2[back][0]
        ny3 = y + dxy2[back][1]
        if room[nx3][ny3] == 1:
            break
        else:
            dq.append([nx3, ny3, direction])

print(ans)

