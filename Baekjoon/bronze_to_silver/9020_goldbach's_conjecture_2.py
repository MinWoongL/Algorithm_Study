## 시간초과 안하는 답
from sys import stdin
from math import sqrt

def prime_number(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def find_ans(num1, num2):

    while num1 > 0:
        if prime_number(num1) and prime_number(num2):
            return print(int(num1), int(num2))
        else:
            num1 -= 1
            num2 += 1


T = int(stdin.readline())

for i in range(T):
    n = int(stdin.readline())
    num1 = 0
    num2 = 0
    half_n = n/2

    if half_n%2 == 1:
        num1 = half_n
        num2 = half_n
        find_ans(num1, num2)

    else:
        num1 = half_n-1
        num2 = half_n+1
        find_ans(num1, num2)
