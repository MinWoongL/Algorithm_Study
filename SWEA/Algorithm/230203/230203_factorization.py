# 소인수분해_서울2반_이민웅

T = int(input())


def factorization(n):
    li = []
    num = 2  # 가장 작은 소수부터 시작
    while num <= n:
        if n % num == 0:  # 2로 나누어지면 리스트에 2입력 후 n 값 변경
            li.append(num)
            n = n / num
        else:
            num += 1  # 나누어지지 않을경우 i 값 변경
    return li


for i in range(1, T+1):
    N = int(input())

    ans_li = factorization(N)

    s_di = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    for value in ans_li:
        s_di[value] += 1

    print('#{}'.format(i), end=' ')
    for k in s_di.keys():
        print(s_di[k],end=' ')
    print('')











