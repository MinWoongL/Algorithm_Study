# 18186_라면사기Large_ramen-large
import sys

N, B, C = map(int, input().split())

fac_li = list(map(int, sys.stdin.readline().split()))

sum_of_ramen = sum(fac_li)
ans = 0
idx = 0
while idx < len(fac_li):
    if B > C:
        if idx <= len(fac_li)-3:
            if fac_li[idx] != 0:
                if fac_li[idx+1] != 0 and fac_li[idx+2] != 0 and fac_li[idx+1] <= fac_li[idx+2]:
                    value = min(fac_li[idx], fac_li[idx + 1], fac_li[idx + 2])
                    fac_li[idx] -= value
                    fac_li[idx+1] -= value
                    fac_li[idx+2] -= value
                    ans += (B+2*C)*value
                elif fac_li[idx+1] != 0:
                    fac_li[idx] -= 1
                    fac_li[idx+1] -= 1
                    ans += (B+C)
                else:
                    ans += B*fac_li[idx]
                    fac_li[idx] = 0
            else:
                while fac_li[idx] == 0:
                    idx += 1
        elif idx == len(fac_li)-2:
            if fac_li[idx+1] != 0:
                value = min(fac_li[idx], fac_li[idx + 1])
                fac_li[idx] -= value
                fac_li[idx + 1] -= value
                ans += (B + C) * value
                idx += 1
            else:
                ans += B * fac_li[idx]
                fac_li[idx] = 0
                idx += 1
        else:
            ans += B * fac_li[idx]
            fac_li[idx] = 0
            idx += 1
    else:
        ans = sum_of_ramen*B
        idx = len(fac_li)

print(ans)
