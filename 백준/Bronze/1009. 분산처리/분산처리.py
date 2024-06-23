import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    a = a % 10
    tmp = 1
    while b > 0:
        if b % 2:
            tmp = (tmp * a) % 10
        b //= 2
        a = (a*a) % 10
    if tmp == 0:
        print(10)
    else:
        print(tmp)