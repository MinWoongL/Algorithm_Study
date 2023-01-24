# 1018_체스판 다시 칠하기

N, M = map(int, input().split())

chess_mat = [list(input()) for _ in range(N)]

count_li = []

# 검은색, 흰색영역 구분 때 % 를 이용해서 하면 간결해짐
for i in range(N-7):
    for j in range(M-7):
        idx1 = 0
        idx2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 1:  # 나머지가 1인 좌표 = 기준점과 색이 다른 좌표
                    if chess_mat[x][y] != 'B':
                        idx1 += 1
                    if chess_mat[x][y] != 'W':
                        idx2 += 1
                else:  # 기준점과 색이 같은좌표
                    if chess_mat[x][y] != 'W':
                        idx1 += 1
                    if chess_mat[x][y] != 'B':
                        idx2 += 1
            # 기준점이 검은색일때, 하얀색일때 모두 체크해야함 (각각 if문과 else문)
        count_li.append(min(idx1, idx2))

count_li.sort()
print(count_li[0])

#  이 경우에 시작점을 바꾸는게 최솟값인 경우를 판단하지 못함 + 이유를 모르겠는 오답출력도 있음
# for i in range(N - 7):
#     for j in range(M - 7):
#         count = 0
#         if chess_mat[i][j] == 'B':
#             for x in range(0, 8, 2):
#                 for y in range(0, 8, 2):
#                     if chess_mat[i + x][j + y] == 'W':
#                         count += 1
#                     elif chess_mat[i + x][j + y + 1] == 'B':
#                         count += 1
#             for x in range(1, 8, 2):
#                 for y in range(0, 8, 2):
#                     if chess_mat[i + x][j + y] == 'B':
#                         count += 1
#                     elif chess_mat[i + x][j + y + 1] == 'W':
#                         count += 1
#         elif chess_mat[i][j] == 'W':
#             for x in range(0, 8, 2):
#                 for y in range(0, 8, 2):
#                     if chess_mat[i + x][j + y] == 'B':
#                         count += 1
#                     elif chess_mat[i + x][j + y + 1] == 'W':
#                         count += 1
#             for x in range(1, 8, 2):
#                 for y in range(0, 8, 2):
#                     if chess_mat[i + x][j + y] == 'W':
#                         count += 1
#                     elif chess_mat[i + x][j + y + 1] == 'B':
#                         count += 1
#         count_li.append(count)
