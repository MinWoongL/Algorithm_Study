#  10870_피보나치5_fibonacci5

def fibonacci(n):
    if n == 0:  #  0 인 경우를 판별해야 RecursionError가 나오지 않음
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


N = int(input())

print(fibonacci(N))
