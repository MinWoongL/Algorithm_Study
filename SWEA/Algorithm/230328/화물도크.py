# SWEA_화물도크


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    time = []
    q = []
    for _ in range(N):
        s, g = map(int, input().split())
        time.append([s, g])
    time.sort(key=lambda x: x[1])

    q.append(time[0][1])
    for i in range(1, N):
        if time[i][0] >= q[-1]:
            q.append(time[i][1])
    print(f'#{tc} {len(q)}')
