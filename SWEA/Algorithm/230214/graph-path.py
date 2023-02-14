# 그래프경로_서울2반_이민웅

def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # graph_mat = [[0]*(V+1) for _ in range(V+1)]
    graph_lst = [[] for _ in range(V+1)]

    visited = [False] * len(graph_lst)

    for _ in range(E):
        graph_li = list(map(int, input().split()))
        v1, v2 = graph_li[0], graph_li[1]
        # graph_mat[v1][v2] = 1
        # graph_mat[v2][v1] = 1

        graph_lst[v1].append(v2)

    check = list(map(int, input().split()))

    dfs(graph_lst, check[0], visited)
    if visited[check[1]]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
