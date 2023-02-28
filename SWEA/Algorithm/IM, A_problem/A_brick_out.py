# A_벽돌깨기_서울2반_이민웅
from itertools import product
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def block_boom(x, y):
    pass


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    block_field = [list(map(int, input().split())) for _ in range(H)]
    w_li = [i for i in range(W)]
    N_comb = product(w_li, repeat=N)
    for v in N_comb:
        print(v)

    for case in N_comb:
        pass


