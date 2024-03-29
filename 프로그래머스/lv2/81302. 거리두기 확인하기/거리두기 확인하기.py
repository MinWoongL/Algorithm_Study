from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(places):
    answer = []
    for room in places:
        mat = []
        for i in range(5):
            q = []
            for j in range(5):
                q.append(room[i][j])
            mat.append(q)
        ans = 1
        for i in range(5):
            if ans == 0:
                break
            for j in range(5):
                if mat[i][j] == 'P':
                    visited = [[0]*5 for _ in range(5)]
                    visited[i][j] = 1
                    q = deque()
                    q.append([i, j, 0])
                    while q:
                        x, y, dis = q.popleft()
                        if dis > 1:
                            continue
                        for d in dxy:
                            nx = x+d[0]
                            ny = y+d[1]
                            if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[nx][ny] == 0:
                                if mat[nx][ny] == 'O':
                                    visited[nx][ny] = 1
                                    q.append([nx, ny, dis+1])
                                elif mat[nx][ny] == 'P':
                                    ans = 0
                                    break
                                else:
                                    visited[nx][ny] = 1
                                    continue
        answer.append(ans)

    return answer