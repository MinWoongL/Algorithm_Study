# 풍선팡_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    max_value = 0
    for i in range(n):
        for j in range(m):
            for c in range(1, mat[i][j]+1):
                if 0 <= i-c < n:
                    ans += mat[i-c][j]
                if 0 <= i+c < n:
                    ans += mat[i+c][j]

                if 0 <= j-c < m:
                    ans += mat[i][j-c]
                if 0 <= j+c < m:
                    ans += mat[i][j+c]
            ans += mat[i][j]

            if ans >= max_value:
                max_value = ans
            ans = 0

    print(f'#{tc} {max_value}')