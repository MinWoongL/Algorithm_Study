# subtree_서울2반_이민웅
# def f(i, a, N): # a 첫번째 왼쪽 조상의 값
#     if i > N:
#         return 0
#     else:
#         l = f(i*2, a, N)
#         tree[i] = l+a+1
#         r = f(i*2+1, tree[i], N)
#         return l + r + 1
def preorder(n):
    global cnt
    if n > 0:
        cnt += 1
        preorder(child1[n])
        preorder(child2[n])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())

    adjL = [[] for _ in range(E + 2)]

    node_li = list(map(int, input().split()))
    cnt = 0
    V = E + 1  # 노드의 개수

    child1 = [0] * (V+1)
    child2 = [0] * (V+1)

    for i in range(E):
        if child1[node_li[i*2]] == 0:
            child1[node_li[i*2]] = node_li[i*2+1]
        else:
            child2[node_li[i*2]] = node_li[i*2+1]

    preorder(N)

    print(f'#{tc} {cnt}')

