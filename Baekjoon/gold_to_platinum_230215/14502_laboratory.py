# 14502_연구소_laboratory
import sys
from itertools import combinations
import copy

input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


#  virus(2 좌표)의 위치부터 0을 만나면 모두 감염(dfs)
def infection(x, y):
    global test_mat
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
            if test_mat[nx][ny] == 0:
                test_mat[nx][ny] = 2
                infection(nx, ny)


N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
# 0 좌표 모두 기록 후 벽을 세울 수 있는 모든 경우의 수 조합
area_for_wall = [(a, b) for a in range(N) for b in range(M) if mat[a][b] == 0]
# 바이러스 좌표 리스트
virus = []
# 벽이 세워지는 경우의 수
wall_combi = combinations(area_for_wall, 3)
ans = 0
# 바이러스 좌표 저장
for i in range(N):
    for j in range(M):
        if mat[i][j] == 2:
            virus.append([i, j])

# 벽이 세워지는 모든 경우에 대해 테스트
for case in wall_combi:
    wall_li = []
    cnt = 0
    # 벽 세움
    for v in case:
        wall_li.append(v)
        x, y = v[0], v[1]
        mat[x][y] = 1
    # test_mat = [[mat[i][j] for j in range(M)] for i in range(N)]
    test_mat = copy.deepcopy(mat)  # 처음에 copy로 했을 때 갱신이 안돼서 deepcopy 사용
    for vi in virus:
        infection(vi[0], vi[1])

    # 감염되지 않은 영역 체크
    for k in range(N):
        for l in range(M):
            if test_mat[k][l] == 0:
                cnt += 1

    if ans < cnt:
        ans = cnt

    # 세운 벽 다시 초기화
    for v in case:
        mat[v[0]][v[1]] = 0

print(ans)
