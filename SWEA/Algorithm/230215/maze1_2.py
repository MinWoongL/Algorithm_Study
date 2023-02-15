T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]
    x, y = 0, 0
    dxy = [-1, 1]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                x = i
                y = j
                break
    stack = [(x, y)]
    ans = 0
    while stack:
        lx, ly = stack.pop()
        if mat[lx][ly] == 3:
            ans = 1
            break
        for value in dxy:
            dx = lx + value
            if 0 <= dx < N:
                if mat[dx][ly] != 1:
                    stack.append((dx, ly))
            dy = ly + value
            if 0 <= dy < N:
                if mat[lx][dy] != 1:
                    stack.append((lx, dy))
        if stack:
            mat[lx][ly] = 1
        else:
            break

    print("#{} {}".format(tc, ans))

