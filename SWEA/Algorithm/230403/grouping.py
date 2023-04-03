# SWEA_그룹나누기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    node_li = list(map(int, input().split()))
    adjL = [[] for _ in range(N+1)]

    for i in range(M):
        n1, n2 = node_li[2*i], node_li[2*i + 1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    ans = 0
    visited = [0]*(N+1)
    for i in range(1, N+1):
        if not visited[i]:
            stack = [i]
            visited[i] = 1
            while stack:
                node = stack.pop()

                for j in adjL[node]:
                    if not visited[j]:
                        stack.append(j)
                        visited[j] = 1
            ans += 1
    print(f'#{tc} {ans}')


