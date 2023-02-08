# 문자열의 거울상_서울2반_이민웅
T = int(input())
for tc in range(1, T+1):
    s = str(input())
    ss = s[::-1]
    s_li = []
    for v in ss:
        if v == 'q':
            s_li.append('p')
        elif v == 'p':
            s_li.append('q')
        elif v == 'b':
            s_li.append('d')
        else:
            s_li.append('b')
    print('#{} '.format(tc), end='')
    print(''.join(s_li))
