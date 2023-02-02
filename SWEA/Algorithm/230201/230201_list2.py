# 1일차_min max_서울2반_이민웅

T = int(input())


def mm(n_list):
    min_value = n_list[0]
    max_value = 0
    for v in n_list:
        if v < min_value:
            min_value = v
        if v > max_value:
            max_value = v

    return max_value - min_value


for i in range(1, T+1):
    N = int(input())
    nli = list(map(int, input().split()))
    # print(nli)

    ans = mm(nli)

    print('#{} {}'.format(i, ans))