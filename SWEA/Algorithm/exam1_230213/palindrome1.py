# T = int(input())

def turn_matrix_90(N, matrix):
    matrix_90 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_90[i][j] = matrix[N - 1 - j][i]

    return matrix_90

for tc in range(1, 11):
    N = int(input())

    word_mat = [list(map(str, input())) for v in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            check = True
            for k in range(0, N//2):
                if word_mat[i][j+k] != word_mat[i][j+N-1-k]:
                    break
            else:
                cnt += 1

    word_mat2 = turn_matrix_90(8, word_mat)
    for i in range(8):
        for j in range(8-N+1):
            for k in range(0, N//2):
                if word_mat2[i][j+k] != word_mat2[i][j+N-1-k]:
                    break
            else:
                cnt += 1

    print(f'#{tc} {cnt}')

