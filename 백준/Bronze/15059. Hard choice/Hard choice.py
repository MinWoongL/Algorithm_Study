import sys
input = sys.stdin.readline

C, B, P = map(int, input().split())
c, b, p = map(int, input().split())

ans = max(c-C, 0) + max(b-B, 0) + max(p-P, 0)
print(ans)