# 파리퇴치3_서울2반_이민웅
dxy = [(0, 1), (0,-1), (1, 0), (-1, 0)]
dxy2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def kill_fly_x(x, y, m):
    ans_sum = 0
    ans_sum += mat[x][y]
    for d in dxy2:
        nx = x
        ny = y
        check = m
        while check != 0:
            nx = nx + d[0]
            ny = ny + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                ans_sum += mat[nx][ny]
            check -= 1

    return ans_sum


def kill_fly(x, y, m):
    ans_sum = 0
    ans_sum += mat[x][y]
    for d in dxy:
        nx = x
        ny = y
        check = m
        while check != 0:
            nx = nx + d[0]
            ny = ny + d[1]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                ans_sum += mat[nx][ny]
            check -= 1
    return ans_sum


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            ans1 = kill_fly_x(i, j, M-1)
            if ans1 > ans:
                ans = ans1
            ans2 = kill_fly(i, j, M-1)
            if ans2 > ans:
                ans = ans2

    print(f'#{tc} {ans}')
