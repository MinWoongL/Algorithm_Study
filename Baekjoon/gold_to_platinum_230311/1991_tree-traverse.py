# 1991_트리순회_tree-traverse
import sys
input = sys.stdin.readline

def preorder(node):
    if node != '.':
        pre_lst.append(node)
        preorder(bt[node][0])
        preorder(bt[node][1])

def inorder(node):
    if node != '.':
        inorder(bt[node][0])
        in_lst.append(node)
        inorder(bt[node][1])

def postorder(node):
    if node != '.':
        postorder(bt[node][0])
        postorder(bt[node][1])
        post_lst.append(node)


N = int(input())

bt = {}
pre_lst = []
in_lst = []
post_lst = []
for _ in range(N):
    p, lc, rc = input().split()

    bt[p] = [lc, rc]
preorder('A')
inorder('A')
postorder('A')

print(''.join(pre_lst))
print(''.join(in_lst))
print(''.join(post_lst))
