#  재귀함수 팩토리얼

def factorial(N):
    if N > 1:
        return N * factorial(N-1)
    elif N == 1:
        return 1
    elif N == 0:
        return N+1


N = int(input())

print(factorial(N))
