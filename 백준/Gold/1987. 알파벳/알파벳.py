# 1987_알파벳_Alphabet
import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bt(i, j, arr):
    global visited
    global ans

    if ans == 26:
        return

    if len(arr) > ans:
        ans = len(arr)

    for d in dxy:
        nx = i + d[0]
        ny = j + d[1]
        if 0 <= nx <= R-1 and 0 <= ny <= C-1:
            if mat[nx][ny] not in arr and visited[nx][ny] == 0:
                arr.add(mat[nx][ny])
                visited[nx][ny] = 1
                bt(nx, ny, arr)
                visited[nx][ny] = 0
                arr.discard(mat[nx][ny])


R, C = map(int, input().split())

mat = [list(v for v in input()) for _ in range(R)]

q = set()
visited = [[0]*C for _ in range(R)]
ans = 0

q.add(mat[0][0])
visited[0][0] = 1
# print(visited)

bt(0, 0, q)
print(ans)
