# 파리퇴치_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    max_value = 0
    for i in range(n):
        for j in range(n):
            for x in range(m):
                for y in range(m):
                    if 0 <= i+x < n and 0 <= j+y < n:
                        ans += mat[i + x][j + y]

            if ans >= max_value:
                max_value = ans
            ans = 0

    print(f'#{tc} {max_value}')