import sys
from math import sqrt


def prime_number(n):  # 소수인지 판별
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def find_ans(num1, num2):  # 두수의 차가 가장 소수 도출작은 두
    while num1 > 0:
        if prime_number(num1) and prime_number(num2):
            return print(int(num1), int(num2))
        else:
            num1 -= 1
            num2 += 1


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    half_n = n / 2

    num1 = half_n
    num2 = half_n
    find_ans(num1, num2)