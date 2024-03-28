# 14500_테트로미노_tetromino
import sys
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, 1)]
extra_dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bt(x, y, score, v, l):
    global ans
    if l == 4:
        if score > ans:
            ans = score
        return

    if score + max_value*(4 - l) <= ans:
        return

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if not v[nx][ny]:
                v[nx][ny] = 1
                bt(nx, ny, score+field[nx][ny], v, l+1)
                v[nx][ny] = 0


N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
max_value = max([max(i) for i in field])
ans = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        
        visited[i][j] = 1
        bt(i, j, field[i][j], visited, 1)
        visited[i][j] = 0

        for x in range(4):
            tmp_sum = field[i][j]
            for y in range(4):
                if x == y:
                    continue
                ni = i + extra_dxy[y][0]
                nj = j + extra_dxy[y][1]
                if 0 <= ni < N and 0 <= nj < M:
                    tmp_sum += field[ni][nj]
                else:
                    break
            else:
                ans = max(ans, tmp_sum)

print(ans)