# 고대유적_서울2반_이민웅

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                cnt = 0
                cnt2 = 0
                for k in range(j,M):
                    if mat[i][k] == 1:
                        cnt += 1
                    else:
                        break
                for l in range(i,N):
                    if mat[l][j] == 1:
                        cnt2 += 1
                    else:
                        break
                max_value = max(cnt, cnt2, max_value)

    print(f'#{tc} {max_value}')