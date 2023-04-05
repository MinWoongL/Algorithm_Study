# 11401_이항계수3_binomial-coefficient3
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

p = 1000000007

def f(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % p
    return n


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p


top = f(N)
bot = f(N - K) * f(K) % p

print(top * square(bot, p - 2) % p)
