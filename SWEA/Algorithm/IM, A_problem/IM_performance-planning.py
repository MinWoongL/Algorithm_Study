# 성공적인공연기획_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):

    bacsu = list(map(int, input()))
    cnt = 0
    ans = 0
    for i in range(len(bacsu)):
        if cnt >= i:
            cnt += bacsu[i]
        else:
            ans += (i - cnt)
            cnt += (i - cnt)
            cnt += bacsu[i]

    print(f'#{tc} {ans}')

