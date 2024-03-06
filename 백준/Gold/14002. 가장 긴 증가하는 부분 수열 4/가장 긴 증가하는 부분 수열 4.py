# 12738_가장 긴 증가하는 부분수열3_Longest Incresing Subsequence3
import sys
input = sys.stdin.readline


def bs(lst, num):
    l, r = 0, len(lst)-1

    while l <= r:
        mid = (l + r)//2
        if lst[mid][0] < num:
            l = mid + 1
        else:
            r = mid - 1

    return l


N = int(input())
n_lst = list(map(int, input().split()))

sub = [(n_lst[0], 0)]
parent = [-1]*N

for i in range(1, N):
    tmp = n_lst[i]
    idx = bs(sub, tmp)
    if idx == len(sub):
        sub.append((tmp, i))
    else:
        sub[idx] = (tmp, i)

    if idx > 0:
        parent[i] = sub[idx-1][1]
    else:
        parent[i] = -1

LIS = []
s_idx = sub[-1][1]

while s_idx != -1:
    LIS.append(n_lst[s_idx])
    s_idx = parent[s_idx]
LIS.reverse()

# print(sub)
# print(parent)
print(len(sub))
print(*LIS)