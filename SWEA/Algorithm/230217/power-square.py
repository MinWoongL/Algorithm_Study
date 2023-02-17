# 1217_거듭제곱

def power(n,m):
    if n == 0 or m == 0:
        return 1

    if m % 2 == 0:
        new_n = power(n, m//2)
        return new_n * new_n

    else:
        new_n = power(n, (m-1)//2)
        return (new_n*new_n)*n


for tc in range(1, 11):
    t = int(input())
    N, M = map(int, input().split())

    ans = power(N, M)
    print(f'#{t} {ans}')