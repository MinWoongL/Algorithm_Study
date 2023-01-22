# 1978_소수 찾기

def find_prime_number(li):
    count = 0
    p = True # primenumber 인지 판별
    for value in li:
        if value == 1:
            pass
        elif value == 2 or value == 3:  # 3은 else 문의 for 문에서 range가 2,2 가 되어서 따로판별
            count += 1
        else:
            sqrt_value = int(value ** 0.5)
            for i in range(2, sqrt_value+1):  # 소수는 값의 루트값까지만 나눠지는지 확인하면 판별할 수 있음
                if value % i == 0:
                    p = False  # 루트값까지 한번이라도 나눠지면 break
                    break
                else:
                    p = True
            if p:
                count += 1
    return count


T = int(input())

li = list(map(int,input().split()))

print(find_prime_number(li))

