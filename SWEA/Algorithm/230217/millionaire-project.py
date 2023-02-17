# 1859_백만장자프로젝트_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost_li = list(map(int, input().split()))
    cost_li2 = list(map(int, input().split()))[::-1]
    stack = []
    # profit = 0
    # idx_b = N-1
    # max_value = 0
    #
    # while idx_b >= 0:
    #     if not stack:
    #         stack.append(cost_li[idx_b])
    #         max_value = cost_li[idx_b]
    #     else:
    #         if cost_li[idx_b] > max_value and cost_li[idx_b] > stack[-1]:
    #             while stack:
    #                 profit += (max_value - stack.pop())
    #             max_value = cost_li[idx_b]
    #             stack.append(cost_li[idx_b])
    #         else:
    #             stack.append(cost_li[idx_b])
    #     idx_b -= 1
    #
    # while stack:
    #     profit += (max_value - stack.pop())
    ''' 앞부터 뒤로
    i = ans = 0
    while i < N:
        i_mx = i
        for j in range(i+1, N):
            if cost_li[i_mx]<cost_li[j]:
                i_mx = j
        for j in range(i, i_mx):
            ans += cost_li[i_mx]-cost_li[j]

        i = i_mx + 1

    '''
    # 역으로 받아서 계산 뒤부터 앞으로 -> 시간차이 많이남
    ans = mx = 0
    for value in cost_li2:
        if mx > value:
            ans += mx-value
        else:
            mx = value

    print(f'#{tc} {ans}')
