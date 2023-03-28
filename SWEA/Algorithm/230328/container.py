# SWEA_컨테이너 운반

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    ti.sort(reverse=True)
    wi.sort(reverse=True)

    ans = 0
    idx = 0
    for i in range(M):
        if idx == N:
            break
        while True:
            if idx == N:
                break
            if wi[idx] <= ti[i]:
                ans += wi[idx]
                idx += 1
                break
            else:
                idx += 1

    print(f'#{tc} {ans}')
