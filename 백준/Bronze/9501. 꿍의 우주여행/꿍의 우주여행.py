import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, D = map(int, input().split())
    ans = 0
    for _ in range(N):
        v, f, c = map(int, input().split())
        if (f/c)*v >= D:
            ans += 1

    print(ans)