# optimal-path

def perm(i, k):
    global ans
    global c_li
    if i == k:
        h = [c_li[0], c_li[1]]
        co = [c_li[2], c_li[3]]
        check = 0
        for v in p:
            check += (abs(client[v][0] - h[0]) + abs(client[v][1] - h[1]))
            h = [client[v][0], client[v][1]]

            if check > ans:
                break
        check += (abs(h[0] - co[0]) + abs(h[1] - co[1]))
        if check < ans:
            ans = check
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = n_li[j]
                used[j] = 1
                perm(i + 1, k)
                used[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    n_li = [i for i in range(N)]

    client = [0] * N
    c_li = list(map(int, input().split()))
    for i in range(2, N + 2):
        client[i - 2] = [c_li[2 * i], c_li[2 * i + 1]]

    used = [0] * N
    p = [0] * N

    ans = float('inf')

    perm(0, N)

    print(f'#{tc} {ans}')