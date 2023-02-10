# 회문2_서울2반_이민웅

def matrix_90(N, mat):
    new_mat = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_mat[i][j] = mat[N-1-j][i]

    return new_mat


for tc in range(1, 11):
    T = int(input())
    word_mat = [list(map(str, input())) for _ in range(100)]

    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(99-j):
                if word_mat[i][j] == word_mat[i][99-k]:
                    if j == 0:  # 0 일때 리버스 인덱싱, 0이 아닐때 리버스 인덱싱 따로 해줘야함.
                        r_mat = word_mat[i][99-k::-1]
                    else:
                        r_mat = word_mat[i][99-k:j-1:-1]
                    # print(r_mat)
                    s_mat = word_mat[i][j:100-k:1]
                    # print(s_mat)
                    if s_mat == r_mat:
                        if len(s_mat) >= ans:
                            ans = len(s_mat)

    # 세로 판단
    word_mat = matrix_90(100, word_mat)

    for i in range(100):
        for j in range(100):
            for k in range(99-j):
                if word_mat[i][j] == word_mat[i][99-k]:
                    if j == 0:
                        r_mat = word_mat[i][99-k::-1]
                    else:
                        r_mat = word_mat[i][99-k:j-1:-1]
                    # print(r_mat)
                    s_mat = word_mat[i][j:100-k:1]
                    # print(s_mat)
                    if s_mat == r_mat:
                        if len(s_mat) >= ans:
                            ans = len(s_mat)

    print(f'#{tc} {ans}')
