# 중위순회_서울2반_이민웅
# def f(i, a, N): # a 첫번째 왼쪽 조상의 값
#     if i > N:
#         return 0
#     else:
#         l = f(i*2, a, N)
#         tree[i] = l+a+1
#         r = f(i*2+1, tree[i], N)
#         return l + r + 1

def inorder(start, N):
    global bt
    if start <= N:
        inorder(2*start, N)
        bt.append(start)
        inorder(2*start+1, N)
    return


for tc in range(1, 11):
    N = int(input())

    tree_data = [[] for _ in range(N+1)]
    for i in range(N):
        data = list(map(str, input().split()))
        tree_data[int(data[0])].append(data[1])
    bt = []
    word = []

    inorder(1, N)
    # print(bt)
    # print(tree_data)
    for v in bt:
        word = word + tree_data[v]
    # print(word)
    print(f'#{tc} ',end='')
    print(*word,sep='')


