import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

if len(str(N)) > 3:
    tmp = str(N)[:-2]
else:
    tmp = str(N)[0]

for i in range(100):
    if i < 10:
        check = "0"+str(i)
    else:
        check = str(i)
    if int(tmp + check)%F == 0:
        ans = tmp + check
        break

print(ans[-2:])