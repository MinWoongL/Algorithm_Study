def find_prime_number(M,N):
    li = []  # 소수를 저장할 리스트
    p = True
    for value in range(M,N+1):  # N도 확인해야하니 N+1까지 해야하는것 주의하기
        if value == 1:
            pass
        elif value == 2 or value == 3:
            li.append(value)
        else:
            sqrt_value = int(value ** 0.5)
            for i in range(2, sqrt_value+1):
                if value % i == 0:
                    p = False
                    break
                else:
                    p = True
            if p:
                li.append(value)
    return li

num = list(map(int,input().split()))

ans_li = find_prime_number(num[0], num[1])

for i in ans_li:
    print(i)