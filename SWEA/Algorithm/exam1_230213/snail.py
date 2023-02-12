T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = N * N
    li = [[0 for p in range(N)] for o in range(N)]

    idx = 1
    i, j = 0, 0
    D = 0

    while idx != num + 1:
        if D % 4 == 0:
            while 0 <= j < N and li[i][j] == 0:
                li[i][j] = idx
                j += 1
                idx += 1
            j -= 1
            i += 1
        elif D % 4 == 1:
            while 0 <= i < N and li[i][j] == 0:
                li[i][j] = idx
                i += 1
                idx += 1
            i -= 1
            j -= 1
        elif D % 4 == 2:
            while 0 <= j < N and li[i][j] == 0:
                li[i][j] = idx
                j -= 1
                idx += 1
            j += 1
            i -= 1
        else:
            while 0 <= i < N and li[i][j] == 0:
                li[i][j] = idx
                i -= 1
                idx += 1
            i += 1
            j += 1
        D += 1
    print(f'#{tc}')
    for v in li:
        print(*v)