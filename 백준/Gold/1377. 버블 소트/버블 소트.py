# 1377_버블소트_bubblesort_gold2
import sys

N = int(input())
stack = []
ans = 0
idx = 1
for _ in range(N):
    n = int(input())
    stack.append([n, idx])
    idx += 1

stack.sort(key=lambda x: x[0])

for i in range(N):
    if stack[i][1]-i > ans:
        ans = stack[i][1]-i

print(ans)
