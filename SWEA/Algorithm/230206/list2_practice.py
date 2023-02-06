# List2_연습1_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    mat = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    cal = [-1, 1]
    for i in range(n):
        for j in range(n):
            for c in cal:
                if 0 <= i-c < n:
                    ans += abs(mat[i][j] - mat[i-c][j])

                if 0 <= j-c < n:
                    ans += abs(mat[i][j] - mat[i][j-c])

    print(f'#{tc} {ans}')
