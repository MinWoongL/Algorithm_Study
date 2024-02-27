# 2473_세 용액_three solutions
import sys
input = sys.stdin.readline

N = int(input())

s_lst = list(map(int, input().split()))
s_lst.sort()

ans = float('inf')
cordi = []
for k in range(N):
    a_3 = s_lst[k]
    tmp_ans = float('inf')
    a_1, a_2 = 0, 0
    i, j = 0, N-1
    if ans == 0:
        break

    while i < j:
        if i == k:
            i += 1
        if j == k:
            j -= 1

        if i >= j:
            break

        a, b = s_lst[i], s_lst[j]
        if abs(a+b+a_3) < tmp_ans:
            tmp_ans = abs(a+b+a_3)
            a_1, a_2 = a, b

        if a+b+a_3 > 0:
            j -= 1
        elif a+b+a_3 < 0:
            i += 1
        else:
            break
    if abs(tmp_ans) < ans:
        ans = abs(tmp_ans)
        cordi = [a_1, a_2, a_3]

cordi.sort()
print(*cordi)