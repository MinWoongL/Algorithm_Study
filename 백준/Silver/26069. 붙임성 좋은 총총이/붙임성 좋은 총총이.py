# 26069_붙임성좋은총총이_chongchong
import sys
input = sys.stdin.readline

N = int(input())

name_dict = {'ChongChong': 1}
cnt = 1
for _ in range(N):
    A, B = input().split()
    if A not in name_dict.keys():
        name_dict[A] = 0
    if B not in name_dict.keys():
        name_dict[B] = 0

    if name_dict[A]:
        if not name_dict[B]:
            name_dict[B] = 1
            cnt += 1

    elif name_dict[B]:
        name_dict[A] = 1
        cnt += 1

print(cnt)