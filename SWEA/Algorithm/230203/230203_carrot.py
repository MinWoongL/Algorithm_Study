# 점점 커지는 당근_서울2반_이민웅

T = int(input())

for i in range(1, T+1):
    N = int(input())
    nli = list(map(int, input().split()))

    bigger_carrot = 1
    carrot_li = []
    checker = 1

    for v in nli:
        if carrot_li:
            if carrot_li[-1] < v:
                checker += 1
                if bigger_carrot <= checker:
                    bigger_carrot = checker
            else:
                checker = 1
            carrot_li.append(v)
        else:
            carrot_li.append(v)

    print('#{} {}'.format(i, bigger_carrot))



