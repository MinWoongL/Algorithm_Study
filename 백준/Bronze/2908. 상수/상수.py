import sys
input = sys.stdin.readline

A, B = map(int, input().split())

A = int(str(A)[::-1])
B = int(str(B)[::-1])

print(max(A, B))
