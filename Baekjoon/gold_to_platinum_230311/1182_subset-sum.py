# 1182_subset-sum

N, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1, 1 << N):
    s = 0
    for j in range(N):
        if i & (1 << j):
            s += lst[j]

    if s == K:
        cnt += 1

print(cnt)