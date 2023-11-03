## 백준_ 12865_ 평범한 배낭

N, K = map(int, input().split())  # 물품의 수 N, 최대 무게 K
dp = [[0] * (K + 1) for _ in range(N + 1)]
stuff = []
for _ in range(N):
    W, V = map(int, input().split())  # 현재 넣으려고 하는 무게 W, 가치 V
    stuff.append((W, V))
# for s in stuff:
#     W, V = s
for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = stuff[i-1][0]
        V = stuff[i-1][1]
        # 현재 배낭의 무게를 초과하는 무게라면 안 넣음
        if j < W:
            dp[i][j] = dp[i - 1][j]
        # 현재 물건 안넣고 가치 vs 현재 배낭 무게에서 W만큼 빼보고 더한 가치
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(dp[-1][-1])