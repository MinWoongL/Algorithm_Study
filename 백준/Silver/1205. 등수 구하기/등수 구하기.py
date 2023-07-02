# 1205_등수구하기_check ranking
import sys
input = sys.stdin.readline

N, record, P = map(int, input().split())

if N > 0:
    score = sorted(list(map(int, input().split())), reverse=True)
else:
    score = []

ans = 1
cnt = 1
for i in range(len(score)):
    if ans > P or cnt > P:
        ans = -1
        break
    elif ans == P or cnt == P:
        if score[i] >= record:
            ans = -1
            break
    if score[i] > record:
        ans += 1
        cnt += 1
    elif score[i] == record:
        cnt += 1
    else:
        break

print(ans)