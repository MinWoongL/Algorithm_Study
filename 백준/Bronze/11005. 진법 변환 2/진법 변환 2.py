import sys
input = sys.stdin.readline

N, B = map(int, input().split())
check = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = []
while N:
    ans.append(str(check[N%B]))
    N //= B

ans = ans[::-1]
print(*ans, sep='')