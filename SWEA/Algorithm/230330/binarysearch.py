# SWEA_이진탐색

def binarysearch(arr, n):
    check = ''
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == n:
            return 1
        elif arr[mid] > n:
            end = mid - 1
            if check == '' or check == 'right':
                check = 'left'

            else:
                return 0
        else:
            start = mid + 1
            if check == '' or check == 'left':
                check = 'right'
            else:
                return 0
    return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_li = list(map(int, input().split()))
    A_li.sort()
    B_li = list(map(int, input().split()))
    cnt = 0
    for v in B_li:
        if binarysearch(A_li, v):
            cnt += 1

    print(f'#{tc} {cnt}')

