import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d_lst = []
cnt = 0
for i in range(1, n//2+1):
    if not n % i:
        d_lst.append(i)
        cnt += 1
        if cnt == k:
            print(i)
            break
else:
    if cnt == k-1:
        print(n)
    else:
        print(0)