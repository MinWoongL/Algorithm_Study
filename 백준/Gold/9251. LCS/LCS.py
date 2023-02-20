# 9251_LCS
# Longest Common Subsequence - 최장 공통 부분 수열

s1 = str(input())
s2 = str(input())

dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]


for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])


