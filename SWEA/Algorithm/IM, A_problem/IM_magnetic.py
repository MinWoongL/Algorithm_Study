# IM_Magnetics_서울2반_이민웅

for tc in range(1, 11):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N-1):
        for j in range(N):
            if mat[i][j] == 1:
                check = i+1
                while check < 99 and mat[check][j] == 0:
                    check += 1
                if mat[check][j] == 1:
                    continue
                elif mat[check][j] == 2:
                    cnt += 1

    print(f'#{tc} {cnt}')

