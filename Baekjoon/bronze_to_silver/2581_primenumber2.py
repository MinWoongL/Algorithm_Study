# 소수 : M 이상 N이하 모든 소수들의 합과 최소값

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


M = int(input())
N = int(input())

ans_li = find_prime_number(M, N)

if len(ans_li) == 0:
    print(-1)
else:
    print(sum(ans_li))
    print(ans_li[0])