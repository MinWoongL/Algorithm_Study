# 10844_쉬운계단수_easy-numofstairs
import sys

N = int(input())

dp = [0]*(N+1)
cnt_num = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
cnt_num2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dp[1] = 9
for i in range(2, N+1):
    cnt = 0
    if i % 2 == 0:
        for j in range(10):
            if j == 0 or j == 9:
                cnt += cnt_num[j]
            else:
                cnt += 2*cnt_num[j]
        dp[i] = cnt
        for k in range(10):
            if k == 0:
                cnt_num2[1] += cnt_num[k]
            elif k == 9:
                cnt_num2[8] += cnt_num[k]
            else:
                cnt_num2[k+1] += cnt_num[k]
                cnt_num2[k-1] += cnt_num[k]
        cnt_num = [0]*10
    else:
        for j in range(10):
            if j == 0 or j == 9:
                cnt += cnt_num2[j]
            else:
                cnt += 2*cnt_num2[j]
        dp[i] = cnt
        for k in range(10):
            if k == 0:
                cnt_num[1] += cnt_num2[k]
            elif k == 9:
                cnt_num[8] += cnt_num2[k]
            else:
                cnt_num[k+1] += cnt_num2[k]
                cnt_num[k-1] += cnt_num2[k]
        cnt_num2 = [0] * 10
print(dp[N] % 1000000000)


