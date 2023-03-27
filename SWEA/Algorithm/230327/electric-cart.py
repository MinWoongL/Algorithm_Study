# 서울2반_electric-cart

def perm(i, k):

    if i == k:
        p_li.append(p.copy())
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = n_li[j]
                used[j] = 1
                perm(i+1, k)
                used[j] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    p_li = []
    n_li = [i for i in range(2, N+1)]
    p = [0]*(N-1)
    used = [0]*(N-1)

    perm(0, N-1)
    # print(p_li)
    ans = float('inf')
    for v in p_li:
        check = 0
        check += mat[0][v[0]-1]

        for i in range(len(v)-1):
            check += mat[v[i]-1][v[i+1]-1]

        check += mat[v[-1]-1][0]

        if check < ans:
            ans = check

    print(f'#{tc} {ans}')
