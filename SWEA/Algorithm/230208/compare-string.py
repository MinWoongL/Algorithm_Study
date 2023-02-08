# 문자열비교_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    start = str1[0]

    l = len(str1)
    l2 = len(str2)

    check = False
    for i in range(l2-l+1):
        if str2[i] == start:
            if str2[i:i+l] == str1:
                print(f'#{tc} 1')
                check = True
                break
    if not check:
        print(f'#{tc} 0')
