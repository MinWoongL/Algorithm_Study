# 3653_영화수집_collecting movies
import sys
input = sys.stdin.readline


def build(node, start, end, N):
    if start == end:
        if start <= N:
            seg_tree[node] = 1
        return seg_tree[node]

    mid = (start+end)//2
    left = build(node*2, start, mid, N)
    right = build(node*2+1, mid+1, end, N)
    seg_tree[node] = left + right
    return seg_tree[node]


def update(node, start, end, pos, value):
    if start == end:
        seg_tree[node] = value
        return
    mid = (start+end)//2
    if start <= pos <= mid:
        update(node*2, start, mid, pos, value)
    else:
        update(node*2+1, mid+1, end, pos, value)
    seg_tree[node] = seg_tree[node*2] + seg_tree[node*2+1]
    return


def query(node, start, end, l_limit, r_limit):
    if r_limit < start or l_limit > end:
        return 0
    if l_limit <= start and r_limit >= end:
        return seg_tree[node]

    mid = (start+end)//2
    left = query(node*2, start, mid, l_limit, r_limit)
    right = query(node*2+1, mid+1, end, l_limit, r_limit)

    return left + right


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    movies = list(map(int, input().split()))

    seg_tree = [0]*(4*(N+M))
    build(1, 0, N+M-1, N-1)
    movie_idx = {}
    for i in range(1, N+1):
        movie_idx[i] = N-i
    idx = N+1
    for m in movies:
        tmp = query(1, 0, N+M-1, movie_idx[m]+1, N+M-1)
        update(1, 0, N+M-1, movie_idx[m], 0)
        movie_idx[m] = idx
        idx += 1
        update(1, 0, N+M-1, movie_idx[m], 1)
        print(tmp, end=" ")

