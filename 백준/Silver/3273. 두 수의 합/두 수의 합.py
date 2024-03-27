import sys
input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
X = int(input())

i, j = 0, N-1

ans = 0
while i < j:
    if n_lst[i] + n_lst[j] == X:
        ans += 1

    if n_lst[i] + n_lst[j] > X:
        j -= 1
    else:
        i += 1

print(ans)