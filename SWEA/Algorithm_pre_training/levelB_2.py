# Sum 최대값 구하기
import sys

sys.stdin = open('input.txt', "r")


def horizonsum(li):
    x = 0
    for i in range(100):
        x = max(sum(li[i]), x)

    return x


def verticalsum(li):
    v_sum = 0
    for i in range(100):
        y = 0
        for j in range(100):
            y = y+li[j][i]
        v_sum = max(y, v_sum)

    return v_sum


def diagonalsum(li):
    d_sum = 0
    d_sum2 = 0
    for i in range(100):
        d_sum = d_sum+li[i][i]
        d_sum2 = d_sum2+li[i][99-i]
    d = max(d_sum,d_sum2)

    return d


for i in range(1, 11):
    idx = int(input())
    nlist = [list(map(int, input().split())) for _ in range(100)]

    print("#{} {}".format(idx,max(horizonsum(nlist),verticalsum(nlist),diagonalsum(nlist))))





