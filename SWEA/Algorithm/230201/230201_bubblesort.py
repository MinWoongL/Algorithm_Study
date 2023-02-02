# 1일차_숫자를 정렬하자_서울2반_이민웅

def b_sort(li, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

                # print(li)
    return li


T = int(input())

for i in range(1, T+1):
    N = int(input())

    nli = list(map(int, input().split()))
    ans = b_sort(nli, N)
    # print(*ans)
    print('#{}'.format(i), *ans)







