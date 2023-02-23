
def n_queen_2(i):
    global ans
    if i == N:
        ans += 1
        return
    for j in range(1, N+1):
        if column_check[j] or d1[i+j] or d2[i+N-j-1]:
            continue
        column_check[j] = True
        d1[i+j] = True
        d2[i+N-j-1] = True
        n_queen_2(i+1)
        column_check[j] = False
        d1[i + j] = False
        d2[i + N - j - 1] = False


N = int(input())
column_check = [False for _ in range(N+1)]
d1 = [False for _ in range(2*N)]
d2 = [False for _ in range(2*N)]
# print(column_check)
# print(d1)
ans = 0
n_queen_2(0)
print(ans)