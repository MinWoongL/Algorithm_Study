N = int(input())

star = [[0]*N for _ in range(N)]

for i in range(1, N+1):
    for j in range(i):
        star[i-1][-1-j] = '*'

for s in star:
    for v in range(N):
        if s[v]:
            print(s[v], end='')
        else:
            print(' ', end='')
    print('')