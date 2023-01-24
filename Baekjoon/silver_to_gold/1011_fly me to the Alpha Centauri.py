# 1011_Fly me to the Alpha Centauri 미해결

# x -> y 지점 최소 이동 횟수 구하기, 마지막 이동거리는 1로 고정
# 재귀함수를 쓰면 Recursion Error 나옴
import math


def n_square_sum(n):  # 1 (2) (3 3) (4 4) (5 5 5) (6 6 6) (7 7 7) (8 8 8 8) (9 9 9 9) (10 10 10 10) ...
    # if n == 1:
    #     return 1
    # else:
    #     return (n * n + n_square_sum(n - 1))
    num = 0
    for i in range(1, n+1):
        num += i*i
    return num


# n^2 까지의합+1 이 거리일때 n까지의 합+1 이 최소이동횟수
def n_sum(n):
    # if n == 1:
    #     return 1
    # else:
    #     return n + n_sum(n - 1)
    num = 0
    for i in range(1,n+1):
        num += i
    return num


T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = 1
    ans = 0
    while n_square_sum(n) < distance:
        n += 1

    # print(n_square_sum(n - 1))
    # print(n_square_sum(n))
    #
    # print(n)
    #
    # print(n_sum(n - 1))
    # print(n_sum(n))
    ans = (n_sum(n - 1) + 1) + math.ceil(((distance - (n_square_sum(n - 1) + 1)) / n))
    print(ans)
