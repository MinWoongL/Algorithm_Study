# 2042_구간 합 구하기_prefix multiplying
import sys
input = sys.stdin.readline

def build(node, start, end):
    if start == end:
        segment[node] = n_lst[start]
        return segment[node]

    mid = (start+end)//2
    left = build(node*2, start, mid)
    right = build(node*2+1, mid+1, end)

    segment[node] = (left + right)

    return segment[node]


def update(node, start, end, pos, value):
    if start == end:
        segment[node] = value
        return

    mid = (start+end)//2
    if start <= pos <= mid:
        update(node*2, start, mid, pos, value)
    else:
        update(node*2+1, mid+1, end, pos, value)

    segment[node] = segment[node*2] + segment[node*2+1]
    return segment[node]


def query(node, start, end, l_limit, r_limit):
    if start > r_limit or end < l_limit:
        return 0

    if start >= l_limit and end <= r_limit:
        return segment[node]

    mid = (start+end)//2
    left = query(node*2, start, mid, l_limit, r_limit)
    right = query(node*2+1, mid+1, end, l_limit, r_limit)

    return left + right


N, M, K = map(int, input().split())

n_lst = [int(input()) for _ in range(N)]
segment = [0]*(4*N)
build(1, 0, N-1)

for i in range(M+K):
    a, b, c = map(int, input().split())

    if a == 2:
        print(query(1, 0, N-1, b-1, c-1))
    else:
        update(1, 0, N-1, b-1, c)