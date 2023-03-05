# 러시아 국기 같은 깃발_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(map(str, input())) for _ in range(N)]
    ans = float('inf')
    # wr = 0
    # for i in range(len(flag[0])):
    #     if flag[0][i] != 'W':
    #         wr += 1
    # for i in range(len(flag[N-1])):
    #     if flag[0][i] != 'R':
    #         wr += 1
    wbr = []
    for v in range(0, N):
        w = b = r = 0
        for i in range(len(flag[v])):
            if flag[v][i] == 'W':
                w += 1
            elif flag[v][i] == 'B':
                b += 1
            else:
                r += 1
        wbr.append([M-w, M-b, M-r])

    for w in range(0, N-2):
        for b in range(w+1, N-1):
            changed = 0
            for i in range(w+1):
                changed += wbr[:][i][0]
            for j in range(w+1, b+1):
                changed += wbr[:][j][1]
            for k in range(b+1, N):
                changed += wbr[:][k][2]
            if ans > changed:
                ans = changed
    print(f'#{tc} {ans}')

