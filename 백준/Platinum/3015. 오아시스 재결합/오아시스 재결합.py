# 3015_오아시스재결합_Oasis-reunion
import sys
input = sys.stdin.readline

N = int(input())

fans = []
idx = 0
ans = 0
max_h = 0
while True:
    if idx == N:
        break

    h = int(int(input()))
    if not fans:
        fans.append([h, 1])
        max_h = h
    else:
        if h > fans[-1][0]:
            while fans and fans[-1][0] < h:
                tmp = fans[-1][1]
                ans += tmp
                fans.pop()
            if fans and fans[-1][0] == h:
                tmp = fans[-1][1]
                ans += tmp
                fans[-1][1] += 1
            else:
                fans.append([h, 1])
            if h < max_h:
                ans += 1

        elif h == fans[-1][0]:
            tmp = fans[-1][1]
            ans += tmp
            fans[-1][1] += 1
            if h < max_h:
                ans += 1
        else:
            if fans:
                ans += 1
            fans.append([h, 1])
        if h > max_h:
            max_h = h

    idx += 1


print(ans)
