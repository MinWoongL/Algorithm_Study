# 2357_최솟값과 최댓값
import sys
input = sys.stdin.readline


def build(node, s, e):
    if s == e:
        seg_tree[node] = [n_lst[s], n_lst[s]]
        return

    mid = (s+e)//2
    build(node*2, s, mid)
    build(node*2+1, mid+1, e)

    seg_tree[node] = [max(seg_tree[node*2][0], seg_tree[node*2+1][0]), min(seg_tree[node*2][1], seg_tree[node*2+1][1])]


def query(node, s, e, l_limit, r_limit):
    if r_limit < s or l_limit > e:
        return [0, 1000000000]

    if l_limit <= s and r_limit >= e:
        return seg_tree[node]

    mid = (s+e)//2
    left = query(node*2, s, mid, l_limit, r_limit)
    right = query(node*2+1, mid+1, e, l_limit, r_limit)

    return [max(left[0], right[0]), min(left[1], right[1])]


N, M = map(int, input().split())

seg_tree = [0]*(4*N)
n_lst = [int(input()) for _ in range(N)]
# print(n_lst)
build(1, 0, N-1)
# print(seg_tree)

for _ in range(M):
    a, b = map(int, input().split())
    ans = query(1, 0, N-1, a-1, b-1)
    print(ans[1], ans[0])