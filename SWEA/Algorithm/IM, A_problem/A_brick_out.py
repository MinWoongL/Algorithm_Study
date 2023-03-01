# A_벽돌깨기_서울2반_이민웅
from itertools import combinations, product
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def block_boom(x, y, mat):
    boom = [(x, y, mat[x][y])]
    while boom:
        lx, ly, value = boom.pop()
        mat[lx][ly] = 0
        for d in dxy:
            nx = lx
            ny = ly
            # 몇 칸만큼 길게 지워야하는지 확인
            check = value-1
            while check != 0:
                nx = nx + d[0]
                ny = ny + d[1]
                if 0 <= nx <= H-1 and 0 <= ny <= W-1:
                    if mat[nx][ny] > 1 and mat[nx][ny] not in boom:
                        boom.append((nx, ny, mat[nx][ny]))
                        mat[nx][ny] = 0
                    else:
                        mat[nx][ny] = 0
                    check -= 1
                else:
                    break

    return mat


def block_down(mat):
    for j in range(W):
        block = []
        i = H-1
        while i >= 0:
            if mat[i][j] != 0:
                block.append(mat[i][j])
                mat[i][j] = 0
            i -= 1
        i = H-1
        while block:
            mat[i][j] = block.pop(0)
            i -= 1
    return mat


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    block_field = [list(map(int, input().split())) for _ in range(H)]
    w_li = [i for i in range(W)]
    N_comb = product(w_li, repeat=N)
    # for v in N_comb:
    #     print(v)

    ans = W*H
    for case in N_comb:
        new_block_field = [[block_field[i][j] for j in range(W)] for i in range(H)]
        cnt = 0
        for v in case:
            i = 0
            while i <= H-1 and new_block_field[i][v] == 0:
                i += 1
            if i == H:
                continue
            else:
                new_block_field = block_boom(i, v, new_block_field)
                new_block_field = block_down(new_block_field)

        for i in range(H):
            for j in range(W):
                if new_block_field[i][j] != 0:
                    cnt += 1

        if cnt <= ans:
            ans = cnt
        if cnt == 0:
            break

    print(f'#{tc} {ans}')
