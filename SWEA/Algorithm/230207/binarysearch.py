# 이진탐색_서울2반_이민웅

T = int(input())


def binarysearch(P, n):
    cnt = 1
    start = 1
    end = P
    while start <= end:
        mid = (start + end)//2
        if mid == n:
            return cnt
        elif mid > n:
            end = mid
            cnt += 1
        else:
            start = mid
            cnt += 1
    return cnt


for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    a_ans = binarysearch(P, A)
    b_ans = binarysearch(P, B)

    if a_ans == b_ans:
        print(f'#{tc} 0')
    elif a_ans > b_ans:
        print(f'#{tc} B')
    else:
        print(f'#{tc} A')

