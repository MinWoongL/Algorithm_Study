# 11051_이항계수2_binomial-coefficient2
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

a, b = 1, 1
for i in range(N, N-K, -1):
    a *= i
for j in range(K, 0, -1):
    b *= j

print((a//b)%10007)
