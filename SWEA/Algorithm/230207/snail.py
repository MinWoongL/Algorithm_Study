# 달팽이숫자_서울2반_이민웅

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = N*N
    li = [[0 for p in range(N)] for o in range(N)]

    idx = 1
    i, j = 0, 0
    D = 0
    while idx != num+1:
        checker = 0

        if D % 4 == 0:
            while j<N and checker < N and li[i][j] == 0:
                if li[i][j] == 0:
                    li[i][j] = idx
                    j += 1
                    idx += 1
                else:
                    j += 1
            j -= 1
            i += 1
        elif D % 4 == 1:
            while i<N and checker < N and li[i][j] == 0:
                if li[i][j] == 0:
                    li[i][j] = idx
                    i += 1
                    idx += 1
                else:
                    i += 1
            i -= 1
            j -= 1
        elif D % 4 == 2:
            while j > -1 and checker < N and li[i][j] == 0:
                if li[i][j] == 0:
                    li[i][j] = idx
                    j -= 1
                    idx += 1
                else:
                    j -= 1
            j += 1
            i -= 1
        else:
            while i > -1 and checker < N and li[i][j] == 0:
                if li[i][j] == 0:
                    li[i][j] = idx
                    i -= 1
                    idx += 1
                else:
                    i -= 1
            i += 1
            j += 1
        D += 1
    print(f'#{tc}')
    for v in li:
        print(*v)
