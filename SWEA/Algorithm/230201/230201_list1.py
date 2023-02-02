# 1일차_Gravity_서울2반_이민웅


# 낙차의 최대값을 구하는 함수
def gravity(n_list):
    max_value = 0
    count = len(n_list)-1
    for i in range(len(n_list)):  # list의 모든 값에 대하여
        for j in range(i+1, len(n_list)):  # 해당 값보다 뒤에서 해당값보다 큰경우만 count에서 빼주기
            if n_list[i] <= n_list[j]:
                count -= 1
        if count > max_value:
            max_value = count
        count = len(n_list)-1-(i+1)  # count 최대값은 초기값(len(n_list)-1) - (해당위치)

    return max_value

T = int(input())

for i in range(1, T+1):
    N = int(input())
    nli = list(map(int, input().split()))
    # print(nli)
    # print(N, M)

    ans = gravity(nli)

    print('#{} {}'.format(i, ans))