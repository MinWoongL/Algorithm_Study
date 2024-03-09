# 2239_스도쿠_sudoku
import sys
input = sys.stdin.readline


def board_check(x, y, num, B):
    nx = x//3
    ny = y//3
    for i in range(3*nx, 3*(nx+1)):
        for j in range(3*ny, 3*(ny+1)):
            if B[i][j] == num:
                return False

    for i in range(9):
        if B[i][y] == num:
            return False

    for i in range(9):
        if B[x][i] == num:
            return False

    return True


def end_check(B):
    for i in range(9):
        for j in range(9):
            if B[i][j] == 0:
                return [i, j]
    return False


def bt(board):
    cordi = end_check(board)
    if not cordi:
        return True

    X, Y = cordi

    for k in range(1, 10):
        if board_check(X, Y, k, board):
            board[X][Y] = k
            if bt(board):
                return True
            board[X][Y] = 0

    return False


sudoku = []
for i in range(9):
    sudoku.append(list(map(int, input().strip())))


bt(sudoku)

for line in sudoku:
    print(*line, sep='')
