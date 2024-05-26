# 16953_A->B
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

cnt = 1
while True:
    if B == A:
        break
    if B < A:
        cnt = -1
        break
    if str(B)[-1] == '1':
        B = int(str(B)[:len(str(B))-1])
    else:
        if not B % 2:
            B = B//2
        else:
            cnt = -1
            break
    cnt += 1

print(cnt)