# 6236_용돈관리
import sys
input = sys.stdin.readline

def bs(mid_value):
    cnt = 0
    deposit = 0
    for k in range(N):
        if deposit < s_lst[k]:
            deposit = mid_value
            cnt += 1
            deposit -= s_lst[k]
        else:
            deposit -= s_lst[k]

    if cnt <= M:
        return False
    else:
        return True


N, M = map(int, input().split())

s_lst = []

for _ in range(N):
    s_lst.append(int(input()))

i = max(s_lst)
j = sum(s_lst)
ans = 0
while i <= j:
    mid = (i+j)//2

    if bs(mid):
        i = mid+1
    else:
        ans = j
        j = mid-1


print(ans)

