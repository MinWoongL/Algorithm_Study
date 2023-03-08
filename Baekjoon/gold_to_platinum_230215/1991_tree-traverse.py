# 1991_트리순회_tree-traverse
import sys
input = sys.stdin.readline


def preorder(start, N):
    global bt_pre
    if start <= N:
        if b_tree[start] != 0:
            bt_pre.append(start)
        preorder(2 * start, N)
        preorder(2 * start + 1, N)
    return


def inorder(start, N):
    global bt_in
    if start <= N:
        inorder(2*start, N)
        if b_tree[start] != 0:
            bt_in.append(start)
        inorder(2*start+1, N)
    return


def postorder(start, N):
    global bt_post
    if start <= N:
        postorder(2 * start, N)
        postorder(2 * start + 1, N)
        if b_tree[start] != 0:
            bt_post.append(start)
    return


N = int(input())

# binary_tree = []
b_tree = [0]*(2**(N//2+2)+1)
bt_in = []
bt_pre = []
bt_post = []
for _ in range(N):
    p, c1, c2 = map(str, input().split())

    # binary_tree.append([p, c1, c2])
    if p == 'A':
        b_tree[1] = p
        if c1 != '.':
            b_tree[2*b_tree.index(p)] = c1
        if c2 != '.':
            b_tree[2 * b_tree.index(p)+1] = c2
    else:
        if c1 != '.':
            b_tree[2 * b_tree.index(p)] = c1
        if c2 != '.':
            b_tree[2 * b_tree.index(p) + 1] = c2
# print(b_tree)
preorder(1, (2**(N//2+1)))
inorder(1, (2**(N//2+1)))
postorder(1, (2**(N//2+1)))

for i in range(N):
    print(b_tree[bt_pre[i]], end='')
print()
for i in range(N):
    print(b_tree[bt_in[i]], end='')
print()
for i in range(N):
    print(b_tree[bt_post[i]], end='')

