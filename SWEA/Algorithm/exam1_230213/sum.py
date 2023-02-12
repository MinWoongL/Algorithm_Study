
# T = int(input())

for tc in range(1, 11):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]

    ans = 0

    cnt = 0
    cnt2 = 0
    for i in range(100):
        for j in range(100):
            cnt += mat[i][j]

        if cnt > ans:
            ans = cnt
        cnt = 0

    for i in range(100):
        for j in range(100):
            cnt += mat[j][i]

        if cnt > ans:
            ans = cnt
        cnt = 0

    for i in range(100):
        for j in range(100):
            if i == j:
                cnt += mat[i][j]
            elif i + j == 99:
                cnt2 += mat[i][j]

    if cnt > ans:
        ans = cnt
        cnt = 0
    if cnt2 > ans:
        ans = cnt2
        cnt2 = 0

    print(f'#{tc} {ans}')
