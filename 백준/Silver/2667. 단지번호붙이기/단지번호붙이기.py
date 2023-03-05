# 2667_단지번호붙이기_numbering-house

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())

house = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

group_cnt = 0
sum_of_group = []
q = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1 and not visited[i][j]:
            q.append([i, j])
            visited[i][j] = True
            group_cnt += 1
            house_cnt = 0
            while q:
                x, y = q.pop(0)
                house_cnt += 1
                for d in dxy:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                        if house[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append([nx, ny])
            sum_of_group.append(house_cnt)
print(group_cnt)
sum_of_group.sort()
for v in sum_of_group:
    print(v)
