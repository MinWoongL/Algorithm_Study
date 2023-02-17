# 재미있는 오셀로 게임_서울2반_이민웅 - 구글링참조

T = int(input())
dxy = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
for tc in range(1, T+1):

    N, M = map(int, input().split())

    mat = [[0 for _ in range(N)] for _ in range(N)]

    start_idx = N//2
    mat[start_idx][start_idx] = 2
    mat[start_idx][start_idx-1] = 1
    mat[start_idx-1][start_idx-1] = 2
    mat[start_idx-1][start_idx] = 1

    for _ in range(M):
        othello = list(map(int, input().split()))
        x, y = othello[0]-1, othello[1]-1

        ans_li = []

        for i in range(8):
            dx, dy = dxy[i]
            nx, ny = x + dx, y + dy

            while True:
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    ans_li = []
                    break
                if mat[nx][ny] == 0:
                    ans_li = []
                    break
                if mat[nx][ny] == othello[2]:
                    break
                else:
                    ans_li.append([nx, ny])
                nx += dx
                ny += dy

            for a, b in ans_li:
                if othello[2] == 1:
                    mat[a][b] = 1
                else:
                    mat[a][b] = 2
        mat[x][y] = othello[2]

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                black += 1
            elif mat[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
