# 2447_별찍기_Recursion-starpoint

# 1. *을 찍는방식으로 재귀, 2. 완성된 matrix에서 *을 지우는 방식으로 재귀
# 2번째 방식
def three_star_point2(mat, num_now, num_first):
    if num_now == 1:
        return mat

    star_mat = three_star_point2(mat, num_now//3, num_first)
    for k in range(0, num_now//3):
        for l in range(0, num_now//3):
            for i in range(num_now//3, (num_first-num_now//3), num_now):
                for j in range(num_now//3, (num_first-num_now//3), num_now):
                    star_mat[i+k][j+l] = ' '
    # for star in star_matrix:
    #     print(*star)
    # print('')
    return star_mat


n = int(input())
star_matrix = [['*'for x in range(n)] for y in range(n)]


ans = three_star_point2(star_matrix, n, n)

for star in ans:
    print(*star, end='')
    print('')


