# 숫자배열회전_서울2반_이민웅

def turn_matrix_90(N, matrix):
    matrix_90 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_90[i][j] = matrix[N - 1 - j][i]

    return matrix_90


Tc = int(input())

for i in range(Tc):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = turn_matrix_90(N, matrix)
    ans2 = turn_matrix_90(N, ans)
    ans3 = turn_matrix_90(N, ans2)

    print("#{}".format(i + 1))
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end='')
        print(" ", end="")
        for j in range(N):
            print(ans2[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(ans3[i][j], end="")
        print(" ")