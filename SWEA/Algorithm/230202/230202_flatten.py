# flatten_서울2반_이민웅


for tc in range(1, 11):

    dump = int(input())

    block_li = list(map(int, input().split()))

    while dump != 0:
        max_value = [0, 0]
        min_value = [0, 100]
        for i in range(len(block_li)):
            if block_li[i] >= max_value[1]:
                max_value = [i, block_li[i]]
            if block_li[i] <= min_value[1]:
                min_value = [i, block_li[i]]
        block_li[max_value[0]] -= 1
        block_li[min_value[0]] += 1
        dump -= 1

    M = 0
    m = 100

    for i in range(len(block_li)):
        if block_li[i] >= M:
            M = block_li[i]
        if block_li[i] <= m:
            m = block_li[i]

    print('#{} {}'.format(tc, M-m))
