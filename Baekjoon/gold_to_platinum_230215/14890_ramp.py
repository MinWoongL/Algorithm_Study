# 14890_경사로_ramp
import sys
input = sys.stdin.readline


def road_check(n, l, road):
    visited = [0] * n
    ans = 1
    for i in range(n-1):
        if road[i] == road[i+1]:
            continue
        else:
            if abs(road[i+1] - road[i]) > 1:
                ans = 0
                return ans
            elif road[i] - road[i+1] == -1:
                if (i+1) - l < 0:
                    ans = 0
                    return ans
                else:
                    now = road[i]
                    for j in range(i, i-l, -1):
                        if road[j] == now and visited[j] == 0:
                            visited[j] = 1
                        else:
                            ans = 0
                            return ans
            elif road[i] - road[i+1] == 1:
                if i+l > n-1:
                    ans = 0
                    return ans
                else:
                    now = road[i+1]
                    for j in range(i+1, i+1+l):
                        if road[j] == now and visited[j] == 0:
                            visited[j] = 1
                        else:
                            ans = 0
                            return ans

    return ans


N, L = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
road_cnt = 0

for v in mat:
    r = road_check(N, L, v)
    if r == 1:
        road_cnt += 1

for i in range(N):
    vertical_road = [mat[j][i] for j in range(N)]
    r = road_check(N, L, vertical_road)
    if r == 1:
        road_cnt += 1

print(road_cnt)