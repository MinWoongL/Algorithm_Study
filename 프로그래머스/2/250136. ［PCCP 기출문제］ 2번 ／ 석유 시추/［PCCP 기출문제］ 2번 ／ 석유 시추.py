from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(land):
    answer = 0
    
    h = len(land)
    w = len(land[0])
    
    visited = [[0]*w for _ in range(h)]
    group = [[0]*w for _ in range(h)]
    
    g_idx = 1
    for i in range(h):
        for j in range(w):
            if land[i][j] and not visited[i][j]:
                q = deque()
                tmp = []
                cnt = 0
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    tmp.append((x, y))
                    cnt += 1
                    
                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        
                        if 0 <= nx <= h-1 and 0 <= ny <= w-1:
                            if land[nx][ny] and not visited[nx][ny]:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                for t in tmp:
                    x, y = t
                    group[x][y] = g_idx
                    visited[x][y] = cnt
                g_idx += 1
    
    
    
    for k in range(w):
        tmp_ans = 0
        g_check = set()
        for l in range(h):
            if group[l][k] and group[l][k] not in g_check:
                g_check.add(group[l][k])
                tmp_ans += visited[l][k]
        if tmp_ans > answer:
            answer = tmp_ans
    # print("V =", visited)
    # print("G =", group)
    return answer