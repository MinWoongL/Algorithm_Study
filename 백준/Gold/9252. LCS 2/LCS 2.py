# 9252_LCS2
import sys
input = sys.stdin.readline

def find_lcs(w1, w2):
    len_w1 = len(w1)
    len_w2 = len(w2)
    dp = [["" for _ in range(len_w2 + 1)] for _ in range(len_w1 + 1)]

    for i in range(1, len_w1 + 1):
        for j in range(1, len_w2 + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + w1[i - 1]
            else:
                if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[len_w1][len_w2]


w1 = list(input().strip())
w2 = list(input().strip())
ans = find_lcs(w1, w2)

if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(ans)

