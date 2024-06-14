import sys
input = sys.stdin.readline

T = int(input())


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


for _ in range(T):

    a, b = map(int, input().split())

    g = gcd(a, b)

    ans = a*b//g
    print(ans)