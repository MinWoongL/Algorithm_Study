# 12015_가장긴증가하는부분수열2_the Longest increasing sub sequence
import sys
input = sys.stdin.readline

def bs(lst, value):
    l, r = 0, len(lst)-1
    while l <= r:
        mid = (l+r)//2
        if lst[mid] < value:
            l = mid + 1
        else:
            r = mid - 1
    return l


N = int(input())

s_lst = list(map(int, input().split()))

ans = [s_lst[0]]

for i in range(1, N):
    tmp = s_lst[i]
    bs_idx = bs(ans, tmp)
    if bs_idx == len(ans):
        ans.append(tmp)
    else:
        ans[bs_idx] = tmp

# print(ans)
print(len(ans))
