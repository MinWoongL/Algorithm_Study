# 2749_피보나치수3_fibo3
# ([[1, 1],[1, 0]]^n) x [F1, F0] = [F_n+1, Fn]임을 응용하여 피보나치수를 행렬곱으로 연산하기
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
                ans_mat[k][l] = ans_mat[k][l] % 1000000
    return ans_mat


# 거듭제곱 연산
def mat_pow(mat, n):
    if n == 1:
        return mat
    if n % 2 == 0:
        ans_mat = mat_pow(mat, n // 2)
        return mat_square(ans_mat, ans_mat)
    else:
        ans_mat = mat_pow(mat, n - 1)
        return mat_square(ans_mat, mat)


n = int(sys.stdin.readline())
mat = [[1, 1], [1, 0]]

ans = mat_pow(mat, n)
print(ans[1][0])
