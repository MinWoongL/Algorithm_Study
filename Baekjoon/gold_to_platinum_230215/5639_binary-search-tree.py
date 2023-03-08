# 5639_이진검색트리_binary-search-tree
import sys
input = sys.stdin.readline


# def postorder(start, N):
#     global bt
#     if start <= N:
#         postorder(2 * start, N)  # 왼쪽 자식 노드
#         postorder(2 * start + 1, N)  # 오른쪽 자식 노드
#         bt.append(start)  # 값 넣기

# def post_order(start, end):
#     if start > end:
#         return
#
#     root = pre_order[start]
#     pivot = end + 1
#     for i in range(start+1, end+1):
#         if root < pre_order[i]:
#             pivot = i
#             break
#     post_order(start+1, pivot - 1)
#     post_order(pivot, end)
#     print(root)

def postorder(start, N):
    global pre


    root = pre[start]

    pass


pre = []
while True:
    n = input().rstrip()
    if n == '':
        break
    else:
        pre.append(int(n))

V = len(pre)
bt = []
postorder(1, V)
# if pre_order:
#     post_order(0, len(pre_order) - 1)
print(pre)
print(bt)


