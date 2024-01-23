# 1629_곱셉_multiple
import sys
input = sys.stdin.readline

def mat_multi(num, n):
    if n == 0:
        return 1
    if n == 1:
        return num%C
    half = mat_multi(num, n//2)
    if n % 2:
        return (half*half*num)%C
    else:
        return (half*half)%C

A, B, C = map(int, input().split())

ans = mat_multi(A, B)

print(ans)