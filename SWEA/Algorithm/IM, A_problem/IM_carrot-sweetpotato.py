# 당근밭 옆 고구마밭

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    goguma_li = list(map(int, input().split()))

    group_cnt = 0
    max_value = 0
    ans_li = []
    now = goguma_li[0]

    stack = [goguma_li[0]]

    for i in range(1, N):
        if goguma_li[i] > goguma_li[i-1]:
            now += goguma_li[i]
            stack.append(goguma_li[i])
            if len(stack) == 2:
                group_cnt += 1
            if i == N-1:
                ans_li.append([len(stack), now])
        else:
            ans_li.append([len(stack), now])
            now = goguma_li[i]
            stack.clear()
            stack.append(goguma_li[i])
    ans_li.sort(key=lambda x: (x[0], x[1]), reverse=True)

    if group_cnt == 0:
        print(f'#{tc} {group_cnt} {0}')
    else:
        print(f'#{tc} {group_cnt} {ans_li[0][1]}')

