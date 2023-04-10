#2467_용액_solution
import sys
input = sys.stdin.readline

N = int(input())

s_li = list(map(int, input().split()))

p1 = 0
p2 = N-1
a = b = 0
ans = float('inf')

while p1 < p2:
    s = s_li[p1] + s_li[p2]

    if abs(s) <= ans:
        ans = abs(s)
        a = s_li[p1]
        b = s_li[p2]

    if s == 0:
        break

    if s > 0:
        p2 -= 1
    else:
        p1 += 1

print(a, b)

