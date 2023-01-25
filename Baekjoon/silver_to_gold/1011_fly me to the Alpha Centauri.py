# 1011_Fly me to the Alpha Centauri 미해결

# x -> y 지점 최소 이동 횟수 구하기, 마지막 이동거리는 1로 고정
# 재귀함수를 쓰면 Recursion Error 나옴
import sys
import math
# n^2 까지의합+1 이 거리일때 n까지의 합+1 이 최소이동횟수 <- 가정이 틀림
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
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x

    n = round(math.sqrt(distance)) - 1  # n의 초기값을 크게해주면 시간초과가 나지 않음
    while 2 * n_sum(n) < distance:
        n += 1

    if (distance - 2 * n_sum(n - 1)) <= n:
        ans = 2 * n - 1
    else:
        ans = 2 * n

    print(ans)
    # tli = list(map(int, sys.stdin.readline().split()))
    #
    # x = tli[0]
    # y = tli[1]
    #
    # distance = y - x
    # n = 1
    # ans = 0
    # while 2*n_sum(n) < distance:  # 거리의 합이 n^2까지의 합보다 클때 -> 거리가 2n까지의 합보다 클때까지로 변경
    #     n += 1
    #
    # print(2*n_sum(n - 1))
    # print(2*n_sum(n))
    #
    # print(n)
    #
    # print(n_sum(n - 1))
    # print(n_sum(n))
    # if (distance - 2*n_sum(n-1)) <= n:
    #     ans = 2*n-1
    # else:
    #     ans = 2*n
    # print(ans)
