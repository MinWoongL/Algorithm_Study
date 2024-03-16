# 11505_구간 곱 구하기_the product of each sections
import sys
input = sys.stdin.readline

def build(node, s, e):
    if s == e:
        seg_tree[node] = n_lst[s]
        return

    mid = (s+e)//2
    build(node*2, s, mid)
    build(node*2+1, mid+1, e)

    seg_tree[node] = (seg_tree[node*2]*seg_tree[node*2+1])%1000000007
    return


def query(node, s, e, l_limit, r_limit):
    if r_limit < s or l_limit > e:
        return 1
    if l_limit <= s and r_limit >= e:
        return seg_tree[node]

    mid = (s+e)//2
    left = query(node*2, s, mid, l_limit, r_limit)
    right = query(node*2+1, mid+1, e, l_limit, r_limit)

    return (left*right)%1000000007


def update(node, s_idx, e_idx, idx, value):
    if s_idx == e_idx:
        seg_tree[node] = value
        return

    mid = (s_idx+e_idx)//2

    if s_idx <= idx <= mid:
        update(node*2, s_idx, mid, idx, value)
    else:
        update(node*2+1, mid+1, e_idx, idx, value)

    seg_tree[node] = (seg_tree[node*2]*seg_tree[node*2+1])%1000000007
    return


N, M, K = map(int, input().split())

seg_tree = [0]*(4*N)
n_lst = [int(input()) for _ in range(N)]

build(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        tmp = query(1, 0, N-1, b-1, c-1)
        print(tmp)