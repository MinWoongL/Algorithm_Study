# 10773_제로_zero

# 정수를 저장하는 명령어 스택
import sys

n = int(input())
value = 0
nli = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        value -= nli.pop()
    else:
        value += num
        nli.append(num)

print(value)