# 16946_벽 부수고 이동하기4_Crushing walls and Moving
import sys
input = sys.stdin.readline
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(X, Y, v):
    stack = [[X, Y]]
    v[X][Y] = 1

    cnt = 0
    while stack:
        x, y = stack.pop()
        cnt += 1
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if not v[nx][ny] and not field[nx][ny]:
                    stack.append([nx, ny])
                    v[nx][ny] = 1

    return cnt


N, M = map(int, input().split())

field = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
sum_check = {}
group_idx = 1
for i in range(N):
    tmp = []
    for j in range(M):
        if field[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1

            group_idx += 1
            field[i][j] = group_idx
            cnt = 0
            stack = [[i, j]]

            while stack:
                x, y = stack.pop()
                cnt += 1

                for d in dxy:
                    nx = x + d[0]
                    ny = y + d[1]

                    if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                        if field[nx][ny] == 0 and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            field[nx][ny] = group_idx
                            stack.append([nx, ny])

            sum_check[group_idx] = cnt

# print(field)
# print(sum_check)
ans = []
for i in range(N):
    tmp = []
    for j in range(M):
        if field[i][j] == 1:
            tmp_cnt = 1
            g_check = []
            for d in dxy:
                ni = i + d[0]
                nj = j + d[1]

                if 0 <= ni <= N-1 and 0 <= nj <= M-1:
                    if field[ni][nj] != 1 and field[ni][nj] not in g_check:
                        g_check.append(field[ni][nj])
                        tmp_cnt += sum_check[field[ni][nj]]
            tmp.append(tmp_cnt%10)
        else:
            tmp.append(0)

    ans.append(tmp)

for l in ans:
    print(*l, sep='')
