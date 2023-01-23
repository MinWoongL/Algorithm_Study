n, m = map(int, input().split())

li = [list(map(int, input().split()))for _ in range(2*n)]

li1 = [li[i] for i in range(n)]
li2 = [li[i] for i in range(n, 2*n)]

for i in range(n):
    for j in range(m):
        print(li1[i][j]+li2[i][j], end=' ')
    print('')