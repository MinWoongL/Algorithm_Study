# 11053_가장 긴 증가하는 부분수열_the longest partial sequence


N = int(input())

nli = list(map(int, input().split()))

dp = [0]*(N+1)

# print(dp)

for i in range(N):
    for j in range(i):
        if nli[i] > nli[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp)+1)


