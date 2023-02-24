# 탈주범 검거_서울2반_이민웅

T = int(input())

pipe_dict = {1: [(1, 0), (0, 1), (-1, 0), (0, -1)],
             2: [(1, 0), (-1, 0)],
             3: [(0, 1), (0, -1)],
             4: [(-1, 0), (0, 1)],
             5: [(1, 0), (0, 1)],
             6: [(1, 0), (0, -1)],
             7: [(-1, 0), (0, -1)],
             }

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(N)]

    start = (R, C, 1)
    q = [start]
    ans_li = []
    while q:
        x, y, dis = q.pop(0)
        if [x, y] not in ans_li and dis <= L:
            ans_li.append([x, y])

        if tunnel[x][y] != 0:
            for d in pipe_dict[tunnel[x][y]]:
                tunnel[x][y] = 0
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                    if tunnel[nx][ny] != 0:
                        if (-d[0], -d[1]) in pipe_dict[tunnel[nx][ny]]:  # 반대쪽에서도 내 위치로 이동이 가능할 때
                            q.append((nx, ny, dis + 1))

    print(f'#{tc} {len(ans_li)}')

