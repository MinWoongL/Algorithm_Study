# 카운팅소트_서울2반_이민웅

T = int(input())


for i in range(1, T+1):
    N = int(input())

    nli = list(map(int,input().split()))

    cnt = [0]*30
    for v in nli:
        cnt[v] += 1

    for j in range(1, len(cnt)):
        cnt[j] += cnt[j-1]

    # print(cnt)
    ans_li = [0] * len(nli)
    for k in range(len(nli)):
        cnt[nli[k]] -= 1
        ans_li[cnt[nli[k]]] = nli[k]

    cnt_s = []
    print('#{}'.format(i), end=' ')
    print(*ans_li)

