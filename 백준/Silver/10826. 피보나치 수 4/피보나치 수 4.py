import sys
input = sys.stdin.readline

fibo = [0]*(10001)

fibo[1] = 1

for i in range(2, 10001):
    fibo[i] = fibo[i-1] + fibo[i-2]

N = int(input())

print(fibo[N])