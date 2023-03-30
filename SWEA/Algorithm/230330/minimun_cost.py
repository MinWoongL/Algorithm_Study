# SWEA_최소생산비용

def f(j, N, c):
    global ans
    global v
    if sum(v) == N:
        if c < ans:
            ans = c
        return

    if c >= ans:
        return

    for k in range(N):
        if v[k] == 0:
            v[k] = 1
            f(j+1, N, c+cost[j][k])
            v[k] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cost = [list(map(int, input().split())) for _ in range(N)]

    v = [0]*N
    ans = 99*N*N
    f(0, N, 0)
    print(f'#{tc} {ans}')


