# 1515_수 이어쓰기_continuing numbers
import sys
input = sys.stdin.readline

number = input().rstrip()
length = len(number)

cnt = 1

while True:
    if length == 0:
        break

    check = str(cnt)
    l = len(check)

    for i in range(l):
        if length and number.startswith(check[i]):
            number = number[1:]
            length -= 1

    cnt += 1

print(cnt-1)
