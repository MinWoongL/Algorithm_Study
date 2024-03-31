import sys
input = sys.stdin.readline

prefix = [0]
check = 100000
ans = 0
for _ in range(10):
    tmp = prefix[-1]+int(input())
    prefix.append(tmp)
    if abs(100 - tmp) <= check:
        check = abs(100 - tmp)
        ans = tmp

print(ans)
