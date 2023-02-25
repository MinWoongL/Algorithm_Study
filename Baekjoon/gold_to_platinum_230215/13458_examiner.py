# 13458_시험감독_examiner

N = int(input())

A_li = list(map(int, input().split()))
A_n = len(A_li)
B, C = map(int, input().split())

cnt = 0

for i in range(A_n):
    if A_li[i] <= B:
        cnt += 1
    else:
        cnt += 1
        n_A = A_li[i]-B
        if n_A%C == 0:
            cnt += n_A//C
        else:
            cnt += (n_A//C+1)

print(cnt)
