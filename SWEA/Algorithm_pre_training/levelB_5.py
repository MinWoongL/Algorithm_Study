# 스도쿠 검증
import sys

sys.stdin = open('input.txt', "r")
Tc = int(input())

def sudoku_check(li):
    status = 0
    for i in range(9):
        for j in range(8):
            if li[i][j] == li[i][8]:
                status = 0
            else:
                status = 1
    for i in range(9):
        for j in range(8):
            if li[j][i] == li[8][i]:
                status = 0
            else:
                status = 1
    # for i in range(9):
    #     for j in range(8):
    #         if i % 3 == 0 and j % 3 == 0:
    #             for k in range(i, i+3):
    #                 for l in range(j, j+3):
                #         if li[i][j] == li[k][]
                #
                #
                # if i % 3 == 0 and j % 3 == 0:
                #     square = [0] * 10
                #     for r in range(i, i + 3):
                #         for c in range(j, j + 3):
                #             num = M[r][c]
                #             if square[num]: return 0
                #             square[num] = 1


    return status

for i in range(Tc):
    sudoku = [list(map(int, input().split()))for _ in range(9)]
    print(sudoku)
    ans = sudoku_check(sudoku)
    print(ans)