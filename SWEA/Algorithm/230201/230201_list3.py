# 1일차_구간 합_서울2반_이민웅

T = int(input())


# 구간합의 최대값과 최소값의 차를 구하는 함수
def r_sum(n_list, m):
    min_value = 10000*m  # n의 최대값 곱하기 구간의 수를 초기 최소값으로 설정
    max_value = 0
    value = 0
    for i in range(0, len(n_list)-m+1):
        for j in range(i, i+m):
            value += n_list[j]
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        value = 0

    return max_value - min_value


for i in range(1, T+1):
    N, M = map(int, input().split())
    nli = list(map(int, input().split()))
    # print(nli)
    # print(N, M)

    ans = r_sum(nli, M)

    print('#{} {}'.format(i, ans))