# 줄기세포배양_서울2반_이민웅

T = int(input())
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    #  K=300, M<=50
    mat = [[0]*(M+2*K) for _ in range(M+2*K)]
    cell_grid = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    cell_stack = []
    for i in range(N):
        for j in range(M):
            # mat[K+i][K+j] = cell_grid[i][j]
            if cell_grid[i][j] != 0:
                mat[K + i][K + j] = [cell_grid[i][j], cell_grid[i][j], cell_grid[i][j]]
                cell_stack.append((K+i, K+j))

    # print(cell_stack)
    # print(mat)
    t = 1
    while t <= K:
        cell_check = []
        for v in cell_stack:
            x = v[0]
            y = v[1]
            # 비활성상태 끝
            if mat[x][y][1] == 0:
                # 방금 활성화 된 상태인지 체크
                if mat[x][y][0] == mat[x][y][2]:
                    cell_value = mat[x][y][0]
                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        if mat[nx][ny] == 0:
                            # 새로 세포배양해야 할 위치 저장
                            cell_check.append([nx, ny, cell_value])
                    mat[x][y][0] -= 1
                    # 세포 생존시간 0 이면 사망상태로  (생존시간 1인 세포는 여기서 걸러줘야 함)
                    if mat[x][y][0] == 0:
                        mat[x][y][2] = -1
                else:
                    mat[x][y][0] -= 1
                    # 세포 생존시간 0 이면 사망상태로
                    if mat[x][y][0] == 0:
                        mat[x][y][2] = -1
            # 아직 비활성상태
            elif mat[x][y][1] > 0:
                mat[x][y][1] -= 1

        for cells in cell_check:
            lx, ly, value = cells
            # print(lx, ly, value)
            if mat[lx][ly] == 0:
                mat[lx][ly] = [value, value, value]
                cell_stack.append((lx, ly))
            else:
                if mat[lx][ly][0] < value:
                    mat[lx][ly] = [value, value, value]
        t += 1

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != 0 and mat[i][j][2] != -1:
                cnt += 1

    print(f'#{tc} {cnt}')