# 23968_알고리즘 수업 - 버블 정렬1_bubblesort1

# python3 로 하면 시간초과남
import sys


def b_sort(li, N, k):
    count = 0
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                count += 1
                ans = (li[j], li[j+1])
                # print(li)
            if count == k:
                return ans
    return -1


n, k = map(int, input().split())

nli = list(map(int, sys.stdin.readline().split()))
# print(nli)

answer = b_sort(nli, n, k)
if answer == -1:
    print(answer)
else:
    print(*answer)








