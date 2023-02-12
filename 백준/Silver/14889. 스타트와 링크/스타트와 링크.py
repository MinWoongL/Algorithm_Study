# 14889_스타트와링크_start and link

def comb(li, n):
    result = []
    if n > len(li):
        return result
    if n == 1:
        for i in li:
            result.append([i])
    else:
        for i in range(len(li)-n+1):
            for j in comb(li[i+1:],n-1):
                result.append([li[i]] + j)

    return result


N = int(input())

n_mat = [list(map(int, input().split())) for _ in range(N)]

team_a = 0
team_b = 0

comb_li = [i for i in range(1, N+1)]
comb_li = comb(comb_li, N//2)
# print(comb_li)
idx = 0
ans = 10000000
while idx <= len(comb_li)//2:
    for i in range(len(comb_li[idx])):
        for j in range(i+1, len(comb_li[idx])):
            team_a += n_mat[comb_li[idx][i]-1][comb_li[idx][j]-1]
            team_a += n_mat[comb_li[idx][j]-1][comb_li[idx][i]-1]
    for i in range(len(comb_li[idx])):
        for j in range(i+1, len(comb_li[idx])):
            team_b += n_mat[comb_li[-idx-1][i]-1][comb_li[-idx-1][j]-1]
            team_b += n_mat[comb_li[-idx-1][j]-1][comb_li[-idx-1][i]-1]

    if abs(team_a - team_b) < ans:
        ans = abs(team_a - team_b)
    team_a = 0
    team_b = 0
    idx += 1
print(ans)

