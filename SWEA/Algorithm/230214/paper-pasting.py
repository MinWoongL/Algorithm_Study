# 종이붙이기_서울2반_이민웅

def fibo(n):
    fib = [0]*(n+1)
    fib[1] = 1
    fib[2] = 3
    for i in range(3, n+1):
        fib[i] = fib[i-2]+fib[i-1]+fib[i-2]
    return fib


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N//10

    ans = fibo(n)
    # print(ans)

    print(f'#{tc} {ans[-1]}')