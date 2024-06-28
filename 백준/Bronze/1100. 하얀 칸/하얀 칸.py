import sys
input = sys.stdin.readline

chess = [list(input().strip()) for _ in range(8)]

tmp = chess[0][0]
ans = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
            ans += 1

print(ans)