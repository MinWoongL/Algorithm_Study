# sum_서울2반_이민웅

for tc in range(1, 11):
    n = int(input())

    mat = [list(map(int, input().split())) for _ in range(100)]

    ans = 0
    for i in range(100):
        check = 0
        for j in range(100):
            check += mat[i][j]
        if check >= ans:
            ans = check

    for i in range(100):
        check = 0
        for j in range(100):
            check += mat[j][i]
        if check >= ans:
            ans = check

    digonal_check = 0
    digonal_check2 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                digonal_check += mat[i][j]

    if digonal_check >= ans:
        ans = digonal_check

    for i in range(100):
        for j in range(100):
            if i + j == 99:
                digonal_check2 += mat[i][j]

    if digonal_check2 >= ans:
        ans = digonal_check2

    print(f'#{tc} {ans}')