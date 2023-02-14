# 14888_연산자 끼워넣기_Operator
import sys
from itertools import permutations

N = int(input())

A_li = list(map(int, sys.stdin.readline().split()))

oper = list(map(int, sys.stdin.readline().split()))
oper_li = []

for i in range(1, len(oper)+1):
    if oper[i-1] != 0:
        for j in range(oper[i-1]):
            oper_li.append(i)

l = len(oper_li)

permu_oper = list(permutations(oper_li, l))
# print(A_li)
# print(oper_li)
# print(permu_oper)
min_ans = 1000000000
max_ans = -1000000000
for value in permu_oper:
    ans = A_li[0]
    for i in range(len(value)):
        if value[i] == 1:
            ans = ans + A_li[i+1]
        elif value[i] == 2:
            ans = ans - A_li[i+1]
        elif value[i] == 3:
            ans = ans * A_li[i+1]
        else:
            if ans < 0:
                ans = (abs(ans)//A_li[i+1])*-1
            else:
                ans = ans//A_li[i+1]
    if ans < min_ans:
        min_ans = ans
    if ans > max_ans:
        max_ans = ans

print(max_ans)
print(min_ans)
