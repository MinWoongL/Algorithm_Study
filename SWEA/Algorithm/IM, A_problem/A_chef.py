# 요리사_서울2반_이민웅
from itertools import combinations

# 모든 음식 조합 만들기
def comb(lst, n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for i in lst:
            result.append([i])
    else:
        for i in range(len(lst)-n+1):
            for j in comb(lst[i+1:], n-1):
                result.append([lst[i]]+j)

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    food_mat = [list(map(int, input().split())) for _ in range(N)]

    n_li = [i for i in range(1, N+1)]
    # 모든 음식 조합 만들기
    food_comb = comb(n_li, N//2)

    # print(food_comb)
    # 음식 시너지 값 최대 20000
    ans = 50000
    last = len(food_comb)-1
    for i in range(len(food_comb)//2):
        A = 0
        B = 0
        for j in range(N//2):
            for k in range(N//2):
                A += food_mat[food_comb[i][j]-1][food_comb[i][k]-1]
                B += food_mat[food_comb[last-i][j]-1][food_comb[last-i][k]-1]

        if abs(A-B) < ans:
            ans = abs(A-B)

    print(f'#{tc} {ans}')
