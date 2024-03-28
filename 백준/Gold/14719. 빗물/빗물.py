# 14719_빗물_the rain
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
r_lst = list(map(int, input().split()))

rain_field = [[0]*W for _ in range(H)]
ans = W*H
for i in range(W):
    for j in range(r_lst[i]):
        rain_field[H-j-1][i] = 1
        ans -= 1

for line in rain_field:
    l, r = 0, W-1
    while l <= W-1 and line[l] != 1:
        line[l] = 1
        l += 1
        ans -= 1
    while r >= 0 and line[r] != 1:
        line[r] = 1
        r -= 1
        ans -= 1

print(ans)
