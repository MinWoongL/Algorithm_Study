import sys
input = sys.stdin.readline

def n_factorial(num, n):
    if n == 1 or n == 0:
        return num

    return n*n_factorial(num, n-1)


N = int(input())

ans = n_factorial(1, N)

print(ans)