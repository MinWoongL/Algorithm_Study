# 숫자카드_서울2반_이민웅

T = int(input())

for i in range(1, T+1):
    N = int(input())
    number = list(map(int, input()))

    cnt_li = [0]*10

    for num in number:
        cnt_li[num] += 1

    max_value = 0
    ans = [0, 0]
    for j in range(10):
        if cnt_li[j] > max_value:
            max_value = cnt_li[j]
            ans = [j, cnt_li[j]]
        elif cnt_li[j] == max_value:
            ans[0] = j

    # print(ans[0])
    print('#{} {} {}'.format(i,ans[0],ans[1]))
