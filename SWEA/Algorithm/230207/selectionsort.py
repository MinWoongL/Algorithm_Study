# 선택정렬_서울2반_이민웅

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    nli = list(map(int, input().split()))

    for i in range(N - 1):
        idx = i
        for j in range(i + 1, N):
            if nli[idx] > nli[j]:
                idx = j
        nli[i], nli[idx] = nli[idx], nli[i]

    print('#{}'.format(tc), end=' ')
    print(*nli)