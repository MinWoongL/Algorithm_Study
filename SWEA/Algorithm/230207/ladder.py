# Ladder1_서울2반_이민웅

for tc in range(1, 11):
    N = int(input())

    nli = [list(map(int, input().split())) for _ in range(100)]
    # print(nli)
    idx = 0
    for i in range(100):
        if nli[99][i] == 2:
            idx = i
    # print(idx)
    i = 98
    while i != 0:
        if 0 <= idx <= 99:
            if idx != 0 and nli[i][idx-1] == 1:
                while idx-1 != -1 and nli[i][idx-1] != 0:
                    idx -= 1
                i -= 1
            elif idx != 99 and nli[i][idx+1] == 1:
                while idx+1 != 100 and nli[i][idx+1] != 0:
                    idx += 1
                i -= 1
            else:
                i -= 1
    print('#{} {}'.format(N, idx))
