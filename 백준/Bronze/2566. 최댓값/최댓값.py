matrix = [list(map(int, input().split())) for i in range(9)]

maxx_num = 0
cordi = []

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= maxx_num:
            maxx_num = matrix[i][j]
            cordi.append([i+1, j+1])

# print(matrix[8][8])
# print(matrix[0][0])
print(maxx_num)

print(cordi[-1][0], cordi[-1][1])