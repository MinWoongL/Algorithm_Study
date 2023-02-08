# Ladder2_서울2반_이민웅

for tc in range(1, 11):
    N = int(input())

    nli = [list(map(int, input().split())) for _ in range(100)]

    min_cnt = 10000
    ans = 0
    for d in range(99, -1, -1):
        if nli[99][d] == 1:
            i = 98
            cnt = 0
            check = d
            while i != 0:
                if 0 <= check <= 99:
                    if check != 0 and nli[i][check - 1] == 1:
                        while check - 1 != -1 and nli[i][check - 1] != 0:
                            check -= 1
                            cnt += 1
                        i -= 1
                        cnt += 1
                    elif check != 99 and nli[i][check + 1] == 1:
                        while check + 1 != 100 and nli[i][check + 1] != 0:
                            check += 1
                            cnt += 1
                        i -= 1
                        cnt += 1
                    else:
                        i -= 1
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt
                ans = check

    print('#{} {}'.format(N, ans))
