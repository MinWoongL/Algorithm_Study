# 사각형찾기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                x = 1
                y = 1
                while True:
                    if mat[i+x][j] == 1:
                        x += 1
                    else:
                        break
                while True:
                    if mat[i][j+y] == 1:
                        y += 1
                    else:
                        break
                if x*y > ans:
                    ans = x*y

    print(f'#{tc} {ans}')

