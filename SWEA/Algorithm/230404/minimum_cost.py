# SWEA_최소비용
from collections import deque
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')]*N for _ in range(N)]
    dp[0][0] = 0

    q = deque()
    q.append([0, 0, mat[0][0]])

    while q:
        x, y, cost = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                w = mat[nx][ny] - cost
                if w > 0 and dp[x][y] + w + 1 < dp[nx][ny]:
                    q.append([nx, ny, mat[nx][ny]])
                    dp[nx][ny] = dp[x][y] + w + 1
                elif w <= 0 and dp[nx][ny] > dp[x][y] + 1:  # w <= 0 없으면 왜 안될까
                    q.append([nx, ny, mat[nx][ny]])
                    dp[nx][ny] = dp[x][y] + 1

    print(f'#{tc} {dp[-1][-1]}')
