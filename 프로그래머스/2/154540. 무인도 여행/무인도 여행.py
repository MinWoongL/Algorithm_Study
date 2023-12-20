import sys
# input = sys.stdin.readline
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(maps):
    answer = []
    i_len = len(maps)
    j_len = len(maps[0])
    visited = [[0]*j_len for _ in range(i_len)]
    
    for i in range(i_len):
        for j in range(j_len):
            if not visited[i][j] and maps[i][j] != 'X':
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                tmp = 0
                while q:
                    x, y = q.popleft()
                    tmp += int(maps[x][y])
                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0 <= nx <= i_len-1 and 0 <= ny <= j_len-1:
                            if not visited[nx][ny] and maps[nx][ny] != "X":
                                visited[nx][ny] = 1
                                q.append([nx, ny])
                answer.append(tmp)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer