# 23559_밥_rice
import sys
import heapq
input = sys.stdin.readline

N, X = map(int, input().split())

hq = []
ans = 0

for _ in range(N):
    a, b = map(int, input().split())

    heapq.heappush(hq, (-1*(a-b), a, b))
    ans += b
    X -= 1000


while hq:
    menu, A, B = heapq.heappop(hq)
    menu = menu*-1
    if menu <= 0 or X < 4000:
        break

    ans += menu
    X -= 4000

print(ans)
