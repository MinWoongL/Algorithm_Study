# A_창용 마을 무리의 개수_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p_li = [[]for _ in range(N+1)]

    for _ in range(M):
        p1, p2 = map(int, input().split())
        p_li[p1].append(p2)
        p_li[p2].append(p1)

    visited = [0]*(N+1)

    cnt = 0
    d = 1
    q = []
    for i in range(1, len(p_li)):
        if visited[i] == 0:
            cnt += 1
            q.append((i, d))
            visited[i] = d
        while q:
            value, d = q.pop(0)
            for v in p_li[value]:
                if visited[v] == 0:
                    q.append((v, d+1))
                    visited[v] = (d+1)

    print(f'#{tc} {cnt}')




