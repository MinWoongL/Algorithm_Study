# 11651_좌표정렬하기 2
import sys
input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    a, b = map(int, input().split())

    lst.append([a, b])

lst.sort(key=lambda x: (x[1], x[0]))

for c in lst:
    print(*c)