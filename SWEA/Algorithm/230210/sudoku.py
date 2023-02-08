# 스도쿠 검증_서울2반_이민웅
T = int(input())


def sudoku_check(li):
    status = 1
    for i in range(9):
        for j in range(8):
            for k in range(9):
                if j != k:
                    if li[i][j] == li[i][k]:
                        status = 0
    for i in range(9):
        for j in range(8):
            for k in range(9):
                if j != k:
                    if li[j][i] == li[k][i]:
                        status = 0
    for i in range(9):
        for j in range(8):
            if i % 3 == 0 and j % 3 == 0:
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if k != i or l != j:
                            if li[i][j] == li[k][l]:
                                status = 0

    return status


for i in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku_check(sudoku)
    print("#{} {}".format(i + 1, ans))