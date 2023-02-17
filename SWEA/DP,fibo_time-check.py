# 다이나믹프로그래밍, 재귀 - 피보나치 시간차이

import time


def fibo1(n):  # 재귀 피보나치
    if n <= 2:
        return 1
    else:
        return fibo1(n - 1) + fibo1(n - 2)


d = [0]*1000000


def fibo2(n):  # 재귀를 활용한 DP 피보나치
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo2(n-1) + fibo2(n-2)
    return d[n]


def fibo3(n): # 재귀를 사용하지 않는 DP 피보나치
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]
    return d[n]


for i in range(1, 1000000, 10000):
    s = time.time()
    res = fibo3(i)
    print('idx :', i, 'time :', round(time.time() - s), 'sec')




