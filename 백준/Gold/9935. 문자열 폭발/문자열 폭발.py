# 9935_문자열 폭발
import sys
input = sys.stdin.readline

msg_str = list(input().strip())
boom = list(input().strip())
boom_len = len(boom)
b_check = boom[-1]

ans = []
for s in msg_str:
    if s != b_check:
        ans.append(s)
    else:
        ans.append(s)
        if ans[-1-(boom_len-1):] == boom:
            for i in range(boom_len):
                ans.pop()

if ans:
    print(*ans, sep="")
else:
    print('FRULA')