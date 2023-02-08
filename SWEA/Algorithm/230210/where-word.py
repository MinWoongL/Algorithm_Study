# 어디에단어가들어갈수있을까_서울2반_이민웅

T = int(input())

for tc in range(1, 11):
    N, K = map(int, input().split())

    nli = [list(map(int, input().split())) for _ in range(N)]
    # print(nli)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if nli[i][j] == 1:
                check = True
                check2 = True
                verti = 0
                hori = 0
                for v in range(1, K):
                    if i+v < N and nli[i+v][j] == 1:
                        verti += 1
                        continue
                    else:
                        check = False
                        break

                if verti == K - 1 and i + K < N:
                    if nli[i+K][j] == 1:
                        check = False

                if verti == K-1 and i >= 1:
                    if nli[i-1][j] == 1:
                        check = False

                for v in range(1, K):
                    if j+v < N and nli[i][j+v] == 1:
                        hori += 1
                        continue
                    else:
                        check2 = False
                        break

                if hori == K - 1 and j + K < N:
                    if nli[i][j+K] == 1:
                        check2 = False
                if hori == K-1 and j >= 1:
                    if nli[i][j-1] == 1:
                        check2 = False

                if check:
                    cnt += 1
                if check2:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))
