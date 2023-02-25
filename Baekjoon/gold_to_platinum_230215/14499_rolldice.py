# 14499_주사위굴리기_RollDice
import sys
input = sys.stdin.readline

dxy = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

N, M, x, y, K = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
move_li = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
# 왼, 아, 오, 뒤, 앞, 위
for move in move_li:
    nx = x + dxy[move][0]
    ny = y + dxy[move][1]

    if 0 <= nx <= N-1 and 0 <= ny <= M-1:
        if move == 4:  # 남
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[3], dice[2], dice[5], dice[1], dice[4]
        elif move == 3:  # 북
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[4], dice[2], dice[1], dice[5], dice[3]
        elif move == 2:  # 서
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[2], dice[5], dice[3], dice[4], dice[0]
        else:  # 동
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[0], dice[1], dice[3], dice[4], dice[2]

        if mat[nx][ny] == 0:
            mat[nx][ny] = dice[1]
        else:
            dice[1] = mat[nx][ny]
            mat[nx][ny] = 0

        x = nx
        y = ny
        print(dice[5])
    else:
        continue








