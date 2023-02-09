# 회문3_서울2반_이민웅

def turn_matrix_90(N, matrix):
    matrix_90 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_90[i][j] = matrix[N - 1 - j][i]

    return matrix_90



Tc = int(input())

for tc in range(1, Tc+1):
    N, M = map(int, input().split())

    word_mat = [list(map(str, input())) for v in range(N)]

    ans_li = []
    for i in range(N):
        for j in range(N-M+1):
            check = True
            for k in range(0, M//2):
                if word_mat[i][j+k] != word_mat[i][j+M-1-k]:
                    check = False


            if check:
                ans_li.append([i, j, 0])

    word_mat2 = []
    # 가로에서 회문이 없었을 시 90도 회전 후 다시 검사
    if len(ans_li) == 0:
        word_mat2 = turn_matrix_90(N, word_mat)
        for i in range(N):
            for j in range(N - M + 1):
                check = True
                for k in range(0, M // 2):
                    if word_mat2[i][j+k] != word_mat2[i][j+M - 1 - k]:
                        check = False


                if check:
                    ans_li.append([i, j, 1])

    if ans_li[0][2] == 0:
        print(f'#{tc}',end=' ')
        for v in range(ans_li[0][1], ans_li[0][1] + M):
            print(word_mat[ans_li[0][0]][v], end='')
        print('')
    else:
        print(f'#{tc}', end=' ')
        for v in range(ans_li[0][1], ans_li[0][1] + M):
            print(word_mat2[ans_li[0][0]][v], end='')
        print('')







