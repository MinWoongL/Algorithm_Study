import sys
input = sys.stdin.readline

N, X = map(int, input().split())

ans = -1
for _ in range(N):
    s, e = map(int, input().split())
    if s+e <= X and s > ans:
        ans = s

print(ans)