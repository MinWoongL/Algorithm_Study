
def msort(li):
    if len(li) == 1:
        return li
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left = msort(left)
    right = msort(right)

    s_li = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            s_li.append(right[j])
            j += 1
        else:
            s_li.append(left[i])
            i += 1
    while i < len(left):
        s_li.append(left[i])
        i += 1
    while j < len(right):
        s_li.append(right[j])
        j += 1

    return s_li


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nli = list(map(int, input().split()))

    nli_new = msort(nli)
    ans_li = []
    for i in range(5):
        ans_li.append(nli_new[-i-1])
        ans_li.append(nli_new[i])

    print(f'#{tc} ',end='')
    print(*ans_li, sep=' ')

