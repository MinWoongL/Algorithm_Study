# 25709_1빼기_minus one
import sys
input = sys.stdin.readline

N = list(input().strip())

cnt = 0

while True:
    if not N or int("".join(N)) == 0:
        break

    cnt += 1
    r_idx = -1
    for i in range(len(N)):
        if N[i] == "1":
            r_idx = i
            break

    if r_idx != -1:
        N.pop(r_idx)
        while True:
            if N and N[0] == '0':
                N.pop(0)
            else:
                break
    else:
        tmp = int("".join(N)) - 1
        N = list(str(tmp))

print(cnt)


