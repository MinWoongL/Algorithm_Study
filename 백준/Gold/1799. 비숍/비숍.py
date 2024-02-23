# 1799_비숍_Bishop
import sys
input = sys.stdin.readline
dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def check(x, y, V1, V2):
    if V1[x+y] or V2[x-y+N-1]:
        return False
    else:
        return True


def bt(field, visit1, visit2, score, x, y, color):
    global ans

    if y > N-1:
        x += 1
        if y % 2 == 0:
            y = 1
        else:
            y = 0

    if x == N:
        if score > ans[color]:
            ans[color] = score
        return

    if field[x][y]:
        if not visit1[x+y] and not visit2[x-y+N-1]:
            visit1[x+y] = 1
            visit2[x-y+N-1] = 1
            bt(field, visit1, visit2, score+1, x, y+2, color)
            visit1[x + y] = 0
            visit2[x-y+N-1] = 0


    bt(field, visit1, visit2, score, x, y+2, color)


N = int(input())

chess_field = [list(map(int, input().split())) for _ in range(N)]
visited1 = [0] * (2*N-1)
visited2 = [0] * (2*N-1)
ans = [0, 0]

bt(chess_field, visited1, visited2, 0, 0, 0, 0)
bt(chess_field, visited1, visited2, 0, 0, 1, 1)

# print(ans)
print(sum(ans))