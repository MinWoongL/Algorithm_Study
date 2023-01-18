# 베르트랑 공준 : n 보다 크고 2n 보다 작거나 같은 소수는 적어도 한 개 존재한다.

# 이 문제는 리스트로 받을필요가 없음 시간초과 주의.

# 소수를 구하는 식을 에라토스테네스의 체를 사용해야함

def find_prime_number(n):
    li = [True] * 2 * n  # 2n 길이만큼의 True 리스트 입력
    sqrt_num = int((2 * n) ** 0.5)  # 2n의 루트값까지만 소수 판별
    if n == 1:
        li = [2]
        return li
    else:
        for i in range(2, sqrt_num + 1):
            if li[i]:
                for j in range(i + i, 2 * n, i):
                    li[j] = False
    li = [i for i in range(n + 1, 2 * n) if li[i] == True]  #
    return li


while True:
    num = int(input())
    if num == 0:
        break
    else:
        ans = find_prime_number(num)
        print(len(ans))

''' #  시간초과로 실패한 코드
while True:
    num = int(input())
    count = 0
    p = True
    if num == 0:
        break
    else:
        for value in range(num + 1, 2 * num + 1):  # n보다 크고 2n보다 작거나 같은 조건을 만족하는 범위에 주의, 기존문제들에 비해 필요없는부분이 많음
            sqrt_value = int(value ** 0.5)
            for i in range(2, sqrt_value + 1):
                if value % i == 0:
                    p = False
                    break
                else:
                    p = True
            if p:
                count += 1
    print(count)
'''
