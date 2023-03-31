# SWEA_격자판숫자이어붙이기

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(n, word, x, y):
    global ans
    if n == 7:
        ans.add(word)
        return

    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx <= 3 and 0 <= ny <= 3:
            dfs(n+1, word+mat[nx][ny], nx, ny)


T = int(input())

for tc in range(1, T+1):

    mat = [input().split() for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(1, mat[i][j], i, j)

    cnt = len(ans)
    print(f'#{tc} {cnt}')

