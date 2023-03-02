# 의석이의 세로로 말해요_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    mat = [[0]*15 for _ in range(15)]

    for i in range(5):
        word = list(input())
        for j in range(len(word)):
            mat[i][j] = word[j]

    ans = ''
    for i in range(15):
        for j in range(15):
            if mat[j][i] != 0:
                ans += mat[j][i]
    print(f'#{tc} {ans}')


