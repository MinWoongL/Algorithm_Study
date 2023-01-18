#  소인수 분해
##  1이 입력되었을때, 아무것도 출력하지않는다 라는 조건에서 Runtime error - type error 발생했었음

def factorization(n):
    li = []  # 소인수분해 리스트
    i = 2  # 가장 작은 소수부터 시작
    while i <= n:
        if n % i == 0:  # 2로 나누어지면 리스트에 2입력 후 n 값 변경
            li.append(i)
            n = n/i
        else:
            i += 1  # 나누어지지 않을경우 i 값 변경
    return li


num = int(input())

if num == 1:
    print("")
else:
    ans = factorization(num)
    for v in ans:
        print(v)