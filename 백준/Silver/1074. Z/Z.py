# 1074_Z
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

ans = 0
check = 0

while True:
    if 2**check <= r or 2**check <= c:
        check += 1
    else:
        break
# if check > 1:
while check >= 1:
    r_tmp = False
    c_tmp = False
    if 2**(check-1) <= r < 2**check:
        r_tmp = True

    if 2**(check-1) <= c < 2**check:
        c_tmp = True

    if r_tmp and c_tmp:
        ans += 3*(2**(2*(check-1)))
        r -= 2 ** (check - 1)
        c -= 2 ** (check - 1)
    elif r_tmp:
        ans += 2*(2**(2*(check-1)))
        r -= 2 ** (check - 1)
    elif c_tmp:
        ans += (2**(2*(check-1)))
        c -= 2 ** (check - 1)

    check -= 1
# else:
#     last = [[0, 1], [2, 3]]
#     ans += last[r][c]

print(ans)
