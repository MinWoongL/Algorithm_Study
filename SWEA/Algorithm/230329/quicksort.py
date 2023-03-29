# 퀵 소트

def partition(lst, l, r):
    p = lst[l]
    i = l
    j = r

    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[j], lst[l] = lst[l], lst[j]
    return j


def qsort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        qsort(lst, l, s - 1)  # 왼쪽 구간
        qsort(lst, s + 1, r)  # 오른쪽 구간


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    qsort(A, 0, len(A) - 1)

    print(f'#{tc} {A[N//2]}')
