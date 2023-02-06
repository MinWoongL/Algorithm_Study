# 기차 사이의 파리_서울2반_이민웅

T = int(input())

for i in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print('#{} {}'.format(i, (D / (A + B)) * F))


