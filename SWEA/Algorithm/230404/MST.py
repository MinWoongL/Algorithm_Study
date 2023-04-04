# SWEA_최소신장트리

# i를 포함하는 집합을 찾는 연산
def findset(i):
    while rep[i] != i:
        i = rep[i]
    return i    # rep[i] == i, 자기 자신을 가리키면 대표원소

# x, y를 포함하는 두 집합을 통합하는 연산
def union(x, y):
    rep[findset(y)] = findset(x)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    rep = [i for i in range(V+1)]

    graph = []
    for i in range(E):
        u, v, w = map(int, input().split())
        graph.append([u, v, w])

    graph.sort(key=lambda x:x[2])

    s = 0
    cnt = 0
    for u, v, w in graph:
        if findset(u) != findset(v):
            cnt += 1
            s += w
            union(u, v)
            if cnt == V:
                break
    print(f'#{tc} {s}')