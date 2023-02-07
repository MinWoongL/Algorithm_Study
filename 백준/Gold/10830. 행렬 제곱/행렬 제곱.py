# 10830_행렬제곱_MatrixSquare
import sys


# 행렬곱을 수행하는 함수
def mat_square(mat, mat2):
    length = len(mat[0])
    ans_mat = [list(0 for p in range(length)) for o in range(length)]
    
    # print(mat2)
    for k in range(length):
        for l in range(length):
            for i in range(length):
                ans_mat[k][l] += mat[k][i] * mat2[i][l]
                ans_mat[k][l] = ans_mat[k][l]%1000

    return ans_mat


# 거듭제곱을 효율적으로 연산해야한다
def mat_pow(mat, n):
    if n == 1:
        return mat
    if n%2 == 0:
        ans_mat = mat_pow(mat, n//2)
        return mat_square(ans_mat, ans_mat)
    else:
        ans_mat = mat_pow(mat, n-1)
        return mat_square(ans_mat, mat)


N, B = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = mat_pow(matrix, B)

# print(ans)
if B == 1:
    for v in ans:
        print(*list(map(lambda x: x%1000, [value for value in v])))
else:
    for v in ans:
        print(*list(map(lambda x: x, [value for value in v])))