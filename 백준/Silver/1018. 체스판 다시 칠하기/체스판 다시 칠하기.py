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
            # 기준점이 검은색일때, 하얀색일때 모두 체크해야함
        count_li.append(min(idx1, idx2))

count_li.sort()
print(count_li[0])