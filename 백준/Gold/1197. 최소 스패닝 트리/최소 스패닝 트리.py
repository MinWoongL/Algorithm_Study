import sys
input = sys.stdin.readline

def findset(node):
    # 경로 압축 기법을 적용하여 최상위 부모를 찾고, 경로상의 모든 노드를 직접 최상위 부모에 연결
    if parent[node] != node:
        parent[node] = findset(parent[node])
    return parent[node]

def union(x, y):
    rootX = findset(x)
    rootY = findset(y)
    
    # 랭크 기반 병합을 적용하여 트리의 높이를 최소화
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1

V, E = map(int, input().split())

graph = []
parent = [i for i in range(V+1)]  # 부모 노드 초기화
rank = [0] * (V + 1)  # 랭크(트리의 높이)를 저장할 배열 초기화

for _ in range(E):
    s, g, w = map(int, input().split())
    graph.append([s, g, w])

graph.sort(key=lambda x: x[2])  # 간선을 가중치에 따라 정렬

weight = 0  # 최소 스패닝 트리의 가중치 합계

for e in graph:
    u, v, w = e
    # 사이클이 발생하지 않는 경우에만 간선을 선택
    if findset(u) != findset(v):
        union(u, v)
        weight += w

print(weight)
