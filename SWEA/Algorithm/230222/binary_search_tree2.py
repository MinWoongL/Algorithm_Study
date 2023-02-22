# SWEA 10757. 5176. 이진탐색
# 재영님 코드
# 굳이 노드번호로 트리를 만들 필요가 없다

def inorder(node):
    global data_tree
    global num
    if node < N + 1:
        inorder(2 * node)  # 왼쪽 자식 노드
        num += 1  # 데이터로 넣을 값
        data_tree[node] = num  # 값 넣기
        inorder(2 * node + 1)  # 오른쪽 자식 노드


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 이게 곧 노드 수

    # 중위순회하면서 수를 채우면 이진탐색트리가 된다.
    data_tree = [0] * (N + 1)  # 값을 담을 트리
    num = 0

    inorder(1)  # 루트 노드의 번호는 1. 중위순회
    print(data_tree)

    print(f'#{tc} {data_tree[1]} {data_tree[N // 2]}')