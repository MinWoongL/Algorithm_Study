# 11050_이항계수_binomial-coefficient
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

a, b = 1, 1
for i in range(N, N-K, -1):
    a *= i
for j in range(K, 0, -1):
    b *= j

print(a//b)
