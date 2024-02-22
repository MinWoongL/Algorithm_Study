# 2470_두 용액_Two solutions
import sys
input = sys.stdin.readline

N = int(input())

solutions = list(map(int, input().split()))

solutions.sort()
ans = float('inf')

a_1, a_2 = 0, 0
i, j = 0, N-1

while i < j:
    a, b = solutions[i], solutions[j]
    if abs(a+b) < ans:
        ans = abs(a+b)
        a_1, a_2 = a, b

    if a+b > 0:
        j -= 1
    elif a+b < 0:
        i += 1
    else:
        break

print(a_1, a_2)


