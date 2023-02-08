# 다솔이의 다이아몬드 장식_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    word = str(input())

    l_word = len(word)
    x_length = 5+(l_word-1)*4
    ans_mat = [[0 for v in range(x_length)] for v in range(5)]

    for i in range(5):
        if i == 0 or i == 4:
            for j in range(2, x_length, 4):
                ans_mat[i][j] = '#'
        elif i == 1 or i == 3:
            for j in range(x_length):
                if j%2 == 0:
                    ans_mat[i][j] = '.'
                else:
                    ans_mat[i][j] = '#'
        else:
            for j in range(x_length):
                if j%4 == 0:
                    ans_mat[i][j] = '#'
    word_idx = 0
    for i in range(2, x_length, 4):
        ans_mat[2][i] = word[word_idx]
        word_idx += 1

    for i in range(5):
        for j in range(x_length):
            if ans_mat[i][j] == 0:
                ans_mat[i][j] = '.'

    for li in ans_mat:
        print(*li, sep='')
