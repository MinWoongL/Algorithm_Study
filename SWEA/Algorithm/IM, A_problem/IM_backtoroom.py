# 4408_자기 방으로 돌아가기_back-to-room

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cor = [0]*201
    for _ in range(N):
        s, g = map(int, input().split())
        if g < s:
            s, g = g, s
        if s % 2 == 0:
            s -= 1
        if g % 2 == 0:
            g -= 1
        s //= 2
        g //= 2
        for i in range(s, g+1):
            cor[i] += 1
    max_value = 0
    for v in cor:
        if v > max_value:
            max_value = v
    print(f'#{tc} {max_value}')