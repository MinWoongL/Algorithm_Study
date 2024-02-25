# 9252_LCS2
import sys
input = sys.stdin.readline

w1 = list(input().strip())
w2 = list(input().strip())
len_w1 = len(w1)
len_w2 = len(w2)
dp = [[[0, ''] for _ in range(len_w2+1)] for _ in range(len_w1+1)]


for i in range(1, len_w1+1):
    for j in range(1, len_w2+1):
        if w1[i-1] == w2[j-1]:
            dp[i][j] = [dp[i-1][j-1][0]+1, dp[i-1][j-1][1] + w1[i-1]]
        else:
            if dp[i][j-1][0] >= dp[i-1][j][0]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]


if dp[-1][-1][0] == 0:
    print(0)
else:
    print(dp[-1][-1][0])
    print(dp[-1][-1][1])

