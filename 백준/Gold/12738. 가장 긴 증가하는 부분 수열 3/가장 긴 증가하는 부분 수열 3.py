# 12738_가장 긴 증가하는 부분수열3_Longest Incresing Subsequence3
import sys
input = sys.stdin.readline


def bs(lst, num):
    l, r = 0, len(lst)-1

    while l <= r:
        mid = (l + r)//2
        if lst[mid] < num:
            l = mid + 1
        else:
            r = mid - 1

    return l


N = int(input())
n_lst = list(map(int, input().split()))

sub = [n_lst[0]]

for i in range(1, N):
    tmp = n_lst[i]
    idx = bs(sub, tmp)
    if idx == len(sub):
        sub.append(tmp)
    else:
        sub[idx] = tmp

print(len(sub))