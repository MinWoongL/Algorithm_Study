def sudoku_2(li):
    for lst in li:
        if (len(set(lst))) != 9:
            return 0

    new_mat = list(zip(*li))

    for lst in new_mat:
        if len(set(lst)) != 9:
            return 0

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            lst = li[i][j:j + 3] + li[i + 1][j:j + 3] + li[i + 2][j:j + 3]
            if len(set(lst)) != 9:
                return 0

    return 1


T = int(input())

for i in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku_2(sudoku)
    print("#{} {}".format(i + 1, ans))