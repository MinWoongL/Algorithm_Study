def find_prime_number(n):
    li = [True] * 2*n
    sqrt_num = int((2*n) ** 0.5)
    #    sqrt_num2 = floor(sqrt(n))
    if n == 1:
        li = [2]
        return li
    else:
        for i in range(2, sqrt_num+1):
            if li[i]:
                for j in range(i + i, 2*n, i):
                    li[j] = False
    li = [i for i in range(n+1, 2*n) if li[i] == True]
    return li

while True:
    num = int(input())
    if num == 0:
        break
    else:
        ans = find_prime_number(num)
        print(len(ans))