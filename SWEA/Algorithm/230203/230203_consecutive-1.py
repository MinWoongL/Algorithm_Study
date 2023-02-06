# 연속된1의개수_서울2반_이민웅

T = int(input())

for i in range(1, T+1):
    N = int(input())
    nli = list(map(int,input()))

    max_one = 0
    checker = 0

    for v in nli:
        if v == 1:
            checker += 1
            if checker >= max_one:
                max_one = checker
        else:
            checker = 0

    print('#{} {}'.format(i, max_one))



