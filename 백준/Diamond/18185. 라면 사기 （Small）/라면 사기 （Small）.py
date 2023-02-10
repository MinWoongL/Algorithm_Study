# 18185_라면사기_ramen
import sys

N = int(input())

factory_li = list(map(int, sys.stdin.readline().split()))

sum_of_ramen = sum(factory_li)
ans = 0
idx = 0
while sum_of_ramen != 0:
    if idx + 2 <= len(factory_li)-1:
        while factory_li[idx] != 0:
            if factory_li[idx+1] != 0 and factory_li[idx+2] != 0 and factory_li[idx+1] <= factory_li[idx+2]:
                factory_li[idx] -= 1
                factory_li[idx + 1] -= 1
                factory_li[idx + 2] -= 1
                sum_of_ramen -= 3
                ans += 7
            elif factory_li[idx+1] != 0:
                factory_li[idx] -= 1
                factory_li[idx + 1] -= 1
                sum_of_ramen -= 2
                ans += 5
            else:
                factory_li[idx] -= 1
                sum_of_ramen -= 1
                ans += 3
        while factory_li[idx] == 0 and idx < len(factory_li)-1:
            idx += 1
    elif idx + 1 <= len(factory_li)-1:
        while factory_li[idx] != 0:
            if factory_li[idx+1] != 0:
                factory_li[idx] -= 1
                factory_li[idx + 1] -= 1
                sum_of_ramen -= 2
                ans += 5
            else:
                factory_li[idx] -= 1
                sum_of_ramen -= 1
                ans += 3
        while factory_li[idx] == 0 and idx < len(factory_li)-1:
            idx += 1
    else:
        while factory_li[idx] != 0:
            factory_li[idx] -= 1
            sum_of_ramen -= 1
            ans += 3
print(ans)
