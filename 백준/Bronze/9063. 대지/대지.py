import sys
input = sys.stdin.readline

N = int(input())

mx, my = 10001, 10001
Mx, My = -10001, -10001

for _ in range(N):
    x, y = map(int, input().split())
    if x < mx:
        mx = x
    if x > Mx:
        Mx = x
    if y < my:
        my = y
    if y > My:
        My = y

print((My-my)*(Mx-mx))