# SWEA_전기버스2

def f(N, c, cnt):
    global ans
    if c == N:
        if cnt < ans:
            ans = cnt
        return
    if cnt >= ans:
        return

    battery = b[c]
    for i in range(battery, 0, -1):
        if c + i <= N:
            f(N, c + i, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    b = lst[1:]
    N = lst[0]
    ans = 999
    f(N - 1, 0, 0)
    print(f'#{tc} {ans - 1}')