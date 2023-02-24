# Square-room_서울2반_이민웅

T = int(input())
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for tc in range(1, 1 + T):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    room_num = 0
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            ans = 0
            q = [(i, j, 1)]
            while q:
                x, y, dis = q.pop(0)
                ans = dis
                for d in dxy:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                        if mat[nx][ny] == mat[x][y] + 1:
                            q.append((nx, ny, dis + 1))
            if ans > max_cnt:
                room_num = mat[i][j]
                max_cnt = ans
            elif ans == max_cnt:  # 룸 넘버 낮은값으로 바꿔주지 않아서 틀림
                if room_num > mat[i][j]:
                    room_num = mat[i][j]

    print(f'#{tc} {room_num} {max_cnt}')

