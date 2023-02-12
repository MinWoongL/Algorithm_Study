
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    max_value = 0
    for i in range(n):
        for j in range(m):
            for k in range(1, mat[i][j]+1):
                if 0 <= i-k < n:
                    ans += mat[i-k][j]
                if 0 <= i+k < n:
                    ans += mat[i+k][j]

                if 0 <= j-k < m:
                    ans += mat[i][j-k]
                if 0 <= j+k < m:
                    ans += mat[i][j+k]
            ans += mat[i][j]

            if ans >= max_value:
                max_value = ans
            ans = 0

    print(f'#{tc} {max_value}')

