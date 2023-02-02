# 24416_알고리즘 수업 - 피보나치 수 1

cnt_a = 1
cnt_b = 1


def fib(n):
    global cnt_a
    if n == 1 or n == 2:
        return 1
    else:  # why? else구문에서만 count?
        cnt_a += 1
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global cnt_b
    cnt_b = 1
    ans = 0
    next = 3
    for i in range(3, n):
        cnt_b += 1
        ans, next = next, ans + next

    return ans


N = int(input())
fib(N)
fibonacci(N)
print(cnt_a)
print(cnt_b)