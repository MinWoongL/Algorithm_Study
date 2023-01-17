from sys import stdin
from math import sqrt, floor
import time


def prime_number(n):
    li = [True] * n
    sqrt_num = int(n ** 0.5)
    #    sqrt_num2 = floor(sqrt(n))
    if n == 1:
        return
    elif n == 2:
        li = [2]
    else:
        for i in range(2, sqrt_num + 1):
            if li[i]:
                for j in range(i + i, n, i):
                    li[j] = False
    li = [i for i in range(2, n) if li[i] == True]
    return li


stdin = open("input.txt", 'r')

s = time.time()

T = int(stdin.readline())

for i in range(T):
    n = int(stdin.readline())
    pn = prime_number(n)
    ln = len(prime_number(n))
    num1, num2 = 0, 0
    b = True
    while b:
        for j in range((ln // 2), -1, -1):  # range를 정할 때 더 효율적인 방법은 없을까??
            for k in range((ln // 2), ln - 1):
                if pn[j] + pn[k] > n:
                    break
                elif pn[j] + pn[k] == n:
                    num1 = pn[j]
                    num2 = pn[k]
                    b = False
                    break
            if b is False:
                break

    print(num1, num2)

e = time.time()
print(e - s)
