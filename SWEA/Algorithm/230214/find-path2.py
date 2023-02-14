# 길찾기_서울2반_이민웅 - 중간에 도착점에 도착하면 그만하기

def dfs(graph, v, g, visited):
    if v == g:
        return 1
    else:
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                if dfs(graph, i, g, visited):
                    return 1
        return 0


for tc in range(1, 11):
    T, E = map(int, input().split())

    e_li = list(map(int, input().split()))

    graph_lst = [[] for _ in range(101)]

    visited = [False] * len(graph_lst)

    for j in range(0, E):
        v1, v2 = e_li[j * 2], e_li[j * 2 + 1]
        graph_lst[v1].append(v2)

    ans = dfs(graph_lst, 0, 99, visited)

    print(f'#{tc} {ans}')
