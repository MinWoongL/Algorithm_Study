T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    m_li = list(map(int, input().split()))

    cnt, idx = 0, 0

    while idx < N and cnt != -1:
        for i in range(K+idx, idx, -1):
            if idx + K >= N:
                idx = N
                break

            if i in m_li:
                idx = i
                cnt += 1
                break

            if i == idx + 1:
                cnt = -1
                break

    if cnt == -1:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, cnt))

