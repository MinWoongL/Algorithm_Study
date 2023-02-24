# Contact_서울2반_이민웅

def bfs(v, visited):
    q = [v]

    visited[v] = 1
    last_idx = 0
    while q:
        t = q.pop(0)
        for k in node[t]:
            if visited[k] == 0:
                q.append(k)
                visited[k] = visited[t]+1
                last_idx = k

    idx = 0
    for j in range(99, -1, -1):
        if visited[j] == visited[last_idx]:
            idx = j
            break

    return idx


for tc in range(1, 11):
    L, S = map(int, input().split())
    contact_li = list(map(int, input().split()))
    node = [[] for _ in range(101)]

    visited = [0]*101
    for i in range(L//2):
        v1, v2 = contact_li[i*2], contact_li[i*2+1]
        node[v1].append(v2)

    ans = bfs(S, visited)

    print(f'#{tc} {ans}')

