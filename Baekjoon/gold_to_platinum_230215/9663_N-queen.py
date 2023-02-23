# 9663_N-Queen

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


'''
N = int(input())

mat = [[0 for _ in range(N)] for _ in range(N)]

ans = 0
dij = [(-1, 0), (-1, 1), (-1, -1)]


def q_check(x, y):
    for d in dij:
        # a, b = d[0], d[1]
        nx, ny = x + d[0], y + d[1]
        # print(N)
        while 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if mat[nx][ny] == 1:
                return 0
            nx += d[0]
            ny += d[1]

    return 1


def n_queen(i, k):
    global ans
    if i == k:
        ans += 1
        return
    else:
        for j in range(k):
            if q_check(i, j):
                mat[i][j] = 1
                n_queen(i+1, k)
                mat[i][j] = 0
        return


n_queen(0, N)
print(ans)
'''


