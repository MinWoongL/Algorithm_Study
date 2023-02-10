# 압축풀기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    zipli = []
    for i in range(n):
        A, B = list(map(str, input().split()))
        zipli.append([A, int(B)])

    ans_li = []

    for v in zipli:
        for k in range(v[1]):
            ans_li.append(v[0])

    cnt = len(ans_li)
    line_cnt = 0
    idx = 0

    print('#{}'.format(tc))
    while True:
        if cnt == 0 :
            break
        if line_cnt != 10:
            print(ans_li[idx],end='')
            idx += 1
            line_cnt += 1
            cnt -= 1
        else:
            print('')
            line_cnt = 0
    print('')

