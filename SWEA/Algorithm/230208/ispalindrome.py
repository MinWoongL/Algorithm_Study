# 회문검사_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())

    l = len(str1)
    check = True

    for i in range(l//2):
        if str1[i] != str1[l-i-1]:
            check = False

    if check:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
