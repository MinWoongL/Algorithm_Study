import sys

T = int(input())
li = []

for i in range(T):
    n = int(sys.stdin.readline())  # int로 감싸주어야 함
    li.append(n)
li = sorted(li)

# for v in li:
#     print(v)

for i in range(T):
    print(li[i])