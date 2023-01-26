# 24060_알고리즘 수업_병합정렬_mergesort
import sys

def msort(li):  # 병합정렬
    if len(li) <= 1:
        return li
    mid = (len(li)+1)//2
    l_li = li[:mid]
    r_li = li[mid:]

    l_li = msort(l_li)
    r_li = msort(r_li)

    s_li = []
    i, j = 0, 0
    while i < len(l_li) and j < len(r_li):
        if l_li[i] < r_li[j]:
            s_li.append(l_li[i])
            count.append(l_li[i])
            i += 1
        else:
            s_li.append(r_li[j])
            count.append(r_li[j])
            j += 1
    while i < len(l_li):
        s_li.append(l_li[i])
        count.append((l_li[i]))
        i += 1
    while j < len(r_li):
        s_li.append(r_li[j])
        count.append(r_li[j])
        j += 1
    return s_li


n, k = map(int, sys.stdin.readline().split())

nli = list(map(int, sys.stdin.readline().split()))  # input으로 받으면 메모리 초과
count = []  # 각 회차별 append되는 항목을 알기 위해 선언
msort(nli)

if len(count) < k:
    print(-1)
else:
    print(count[k-1])



