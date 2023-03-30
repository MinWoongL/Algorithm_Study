# SWEA_동철이의 일분배

def dfs(a, p):
    global mat
    global ans
    if sum(visited) == N:
        if p > ans:
            ans = p
        return

    if p <= ans:
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(a+1, p*(mat[a][j]))
            visited[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            mat[i][j] = mat[i][j]/100

    visited = [0]*N
    ans = 0
    dfs(0, 1)
    print("#{} {:.6f}".format(tc, ans*100))