# 최대최소의 간격_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    n_li = list(map(int, input().split()))

    min_value = 100
    min_idx = 0
    max_value = 0
    max_idx = 0
    for i in range(N):
        if n_li[i] < min_value:
            min_value = n_li[i]
            min_idx = i
        if n_li[i] >= max_value:
            max_value = n_li[i]
            max_idx = i

    print(f'#{tc} {abs(max_idx - min_idx)}')

