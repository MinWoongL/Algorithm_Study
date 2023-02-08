# 글자수_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    s_di = {}
    for v in str1:
        if v not in s_di.keys():
            s_di[v] = 0

    max_value = 0
    for v in str2:
        if v in s_di.keys():
            s_di[v] += 1
            if s_di[v] > max_value:
                max_value = s_di[v]

    print(f'#{tc} {max_value}')
