# 길찾기_서울2반_이민웅

def dfs(graph, v, visited):

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for tc in range(1, 11):
    T, E = map(int, input().split())

    e_li = list(map(int, input().split()))

    graph_lst = [[] for _ in range(101)]

    visited = [False] * len(graph_lst)

    for j in range(0, E):
        v1, v2 = e_li[j*2], e_li[j*2+1]
        graph_lst[v1].append(v2)

    dfs(graph_lst, 0, visited)

    if visited[99]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')


