# 현주의상자바꾸기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    lst = [0]*N
    for i in range(1, Q+1):
        s, g = map(int, input().split())
        for v in range(s-1, g):
            lst[v] = i

    print(f'#{tc} ', end='')
    print(*lst, sep=' ')


