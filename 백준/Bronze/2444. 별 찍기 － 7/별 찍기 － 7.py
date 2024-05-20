import sys
input = sys.stdin.readline

N = int(input())

stars = []
for i in range(N):
    tmp = []
    for j in range(N+i):
        if N - 1 - i <= j <= N - 1 + i:
            tmp.append('*')
        else:
            tmp.append(' ')
    stars.append(tmp)

for i in range(N):
    print(*stars[i], sep='')
for i in range(N-2, -1, -1):
    print(*stars[i], sep='')