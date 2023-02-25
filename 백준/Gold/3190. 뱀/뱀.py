# 3190_뱀_snake
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
num_of_apple = int(input())

mat = [[0] * N for _ in range(N)]
for _ in range(num_of_apple):
    x, y = map(int, input().split())
    mat[x-1][y-1] = 1

# print(mat)
L = int(input())
direction = []
for _ in range(L):
    X, C = map(str, input().split())
    direction.append([int(X), C])

direction.append([N+1, 'D'])

t = 0
cnt = 0
d = 0
snake = deque()
snake.append([0, 0])
mat[0][0] = 2
game_over = False
for i in range(L+1):
    if game_over:
        break
    else:
        time = direction[i][0]
        while t != time:
            t += 1
            cnt += 1
            x, y = snake.pop()
            nx = x + dxy[d][0]
            ny = y + dxy[d][1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if mat[nx][ny] == 1:
                    snake.append([x, y])
                    snake.append([nx, ny])
                    mat[nx][ny] = 2
                elif mat[nx][ny] == 0:
                    snake.append([x, y])
                    snake.append([nx, ny])
                    mat[nx][ny] = 2
                    a, b = snake.popleft()
                    mat[a][b] = 0
                else:
                    game_over = True
                    break
            else:
                game_over = True
                break
        if direction[i][1] == 'L':
            d -= 1
            if d == -1:
                d = 3
        else:
            d += 1
            if d == 4:
                d = 0

print(cnt)

