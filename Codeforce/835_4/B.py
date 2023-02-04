# B_Atilla's_Favorite_problem
import sys

T = int(input())

for tc in range(T):
    n = int(sys.stdin.readline())

    word = str(input())

    max_value = 97
    for v in word:
        if ord(v) > max_value:
            max_value = ord(v)
        # print(ord(v))

    max_value -= 96
    print(max_value)
