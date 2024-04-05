# 12789_도키도키 간식드리미
import sys
input = sys.stdin.readline

N = int(input())
*n_lst, = map(int, input().split())

stack = []
number = 1
ans = "Nice"
for i in range(N):
    while stack and stack[-1] == number:
        stack.pop()
        number += 1
    if n_lst[i] == number:
        number += 1
    elif not stack or stack[-1] > n_lst[i]:
        stack.append(n_lst[i])
    else:
        ans = "Sad"
        break


while stack and ans == "Nice":
    tmp = stack.pop()
    if tmp == number:
        number += 1
    else:
        ans = "Sad"
        break

print(ans)