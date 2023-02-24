# 세제곱근을 찾아라_서울2반_이민웅


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    s = 1
    end = N
    ans = 0
    while s <= end:
        m = (s + end) // 2
        if m**3 == N:
            ans = m
            break
        elif m**3 < N:
            s = m + 1
        else:
            end = m - 1
    if ans != 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} -1')

