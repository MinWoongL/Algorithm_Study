# 1003_피보나치함수_fibonacci-func
import sys
input = sys.stdin.readline

dp_zero = [0]*41
dp_one = [0]*41

dp_zero[0] = 1

for i in range(1, 41):
    dp_zero[i], dp_one[i] = dp_one[i-1], dp_zero[i-1] + dp_one[i-1]

T = int(input())

for _ in range(T):
    N = int(input())

    print(dp_zero[N], dp_one[N])
