# SWEA_장훈이의 높은선반

def f(i, cost, s):
    global ans
    if i == N:
        if cost >= B:
            if cost < ans:
                ans = cost
        return
    if cost >= B:
        if cost < ans:
            ans = cost
        return
    if cost + s < B:
        return

    if cost >= ans:
        return

    f(i+1, cost, s-height[i])
    f(i+1, cost+height[i], s-height[i])


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    height = list(map(int, input().split()))
    s = sum(height)
    ans = float('inf')

    f(0, 0, s)
    print(f'#{tc} {ans-B}')