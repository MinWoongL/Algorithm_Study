# 색칠하기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    mat0 = [[0 for i in range(10)] for j in range(10)]
    mat = [list(map(int, input().split())) for _ in range(n)]

    for v in mat:
        if v[4] == 1:
            for x in range(v[0],v[2]+1):
                for y in range(v[1],v[3]+1):
                    if mat0[x][y] == 2 or mat0[x][y] == 3:
                        mat0[x][y] = 3
                    else:
                        mat0[x][y] = 1
        elif v[4] == 2:
            for x in range(v[0],v[2]+1):
                for y in range(v[1],v[3]+1):
                    if mat0[x][y] == 1 or mat0[x][y] == 3:
                        mat0[x][y] = 3
                    else:
                        mat0[x][y] = 2
    ans = 0
    for k in range(10):
        for l in range(10):
            if mat0[k][l] == 3:
                ans += 1

    print(f'#{tc} {ans}')



