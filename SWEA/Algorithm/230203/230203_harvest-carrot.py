# 기차 사이의 파리_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nli = list(map(int, input().split()))

    max_value = 0
    checker = 0
    ans = 10000000
    for v in nli:
        max_value += v
    i = 0

    while max_value >= checker:
        max_value -= nli[i]
        checker += nli[i]
        sub = max_value - checker
        ans = min(abs(ans), abs(sub))
        i += 1

    if abs(ans) < abs(sub):
        i -= 1

    print('#{} {} {}'.format(tc, i, ans))

