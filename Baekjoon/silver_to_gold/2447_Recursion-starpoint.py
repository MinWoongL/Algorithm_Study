# 2447_별찍기_Recursion-starpoint

def three_star_point(matrix):
    ln = len(matrix[0])
    global divide_num
    if divide_num == ln:
        return 1
    else:
        sli_y = ln//divide_num
        while sli_y < ln-sli_y:
            for i in range(sli_y, 2*sli_y):
                sli_x = ln // divide_num
                while sli_x < ln-sli_x:
                    for j in range(sli_x, 2*sli_x):
                        matrix[i][j] = ' '
                    sli_x += ln//divide_num
            sli_y += ln//divide_num

        divide_num = divide_num*3
        return three_star_point(matrix)


n = int(input())

divide_num = 3

star_matrix = [['*'for i in range(n)] for i in range(n)]

three_star_point(star_matrix)

for v in star_matrix:
    print(*v)


# for i in range(n):
#     for j in range(n):
#         if i < n/3:
#             print("*", end='')
#         elif i <= 2*n/3:
#             if j >= n/3 and j < 2*n/3:
#                 print(' ', end='')
#             else:
#                 print('*', end='')
#         else:
#             print('*', end='')
#     print('')