# 1920_수찾기_find-number
import sys
input = sys.stdin.readline


def binary_search(n, li):
    s = 0
    e = len(li)-1
    while s <= e:
        mid = (s+e)//2
        if li[mid] == n:
            return 1
        elif li[mid] > n:
            e = mid-1
        else:
            s = mid+1
    return 0


N = int(input())

n_li = list(map(int, input().split()))
n_li.sort()

M = int(input())
m_li = list(map(int, input().split()))
for v in m_li:
    print(binary_search(v, n_li))
