# 숫자배열회전
import sys

sys.stdin = open('input.txt', "r")

def turn_matrix_90(N, matrix):
    matrix_90 = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_90[i][j] = matrix[N-1-j][i]

    return matrix_90


def turn_matrix_180(N, matrix):
    matrix_180 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_180[i][j] = matrix[N-1-i][N-1-j]

    return matrix_180


def turn_matrix_270(N, matrix):
    matrix_270 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_270[i][j] = matrix[j][N-1-i]

    return matrix_270


Tc = int(input())

for i in range(Tc):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print("#{}".format(i+1))
    for i in range(N):
        for j in range(N):
            print(turn_matrix_90(N,matrix)[i][j],end='')
        print(" ",end="")
        for j in range(N):
            print(turn_matrix_180(N, matrix)[i][j], end="")
        print(" ",end="")
        for j in range(N):
            print(turn_matrix_270(N, matrix)[i][j], end="")
        print(" ")

