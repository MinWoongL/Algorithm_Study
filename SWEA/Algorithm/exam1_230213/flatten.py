
# T = int(input())

for tc in range(1, 11):
    N = int(input())
    box_li = list(map(int, input().split()))

    while N != 0:
        max_value = [0,0]
        min_value = [0,100]
        for i in range(len(box_li)):
            if box_li[i] > max_value[1]:
                max_value = [i, box_li[i]]
            if box_li[i] < min_value[1]:
                min_value = [i, box_li[i]]
        box_li[max_value[0]] -= 1
        box_li[min_value[0]] += 1
        N -= 1

    M = 0
    m = 100
    for v in box_li:
        if v > M:
            M = v
        if v < m:
            m = v
    print(f'#{tc} {M-m}')





