# 1958_LCS3
import sys
input = sys.stdin.readline

def find_lcs(w1, w2, w3):
    len_w1 = len(w1)
    len_w2 = len(w2)
    len_w3 = len(w3)
    dp = [[[0]*(len_w3+1) for _ in range(len_w2 + 1)] for _ in range(len_w1 + 1)]

    for i in range(1, len_w1 + 1):
        for j in range(1, len_w2 + 1):
            for k in range(1, len_w3 + 1):
                if w1[i - 1] == w2[j - 1] and w2[j - 1] == w3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    return dp[-1][-1][-1]


w1 = list(input().strip())
w2 = list(input().strip())
w3 = list(input().strip())

ans = find_lcs(w1, w2, w3)
print(ans)
