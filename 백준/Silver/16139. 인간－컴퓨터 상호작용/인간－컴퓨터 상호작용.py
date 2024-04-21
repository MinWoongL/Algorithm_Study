# 16139_인간-컴퓨터상호작용_Human-computer interaction
import sys
input = sys.stdin.readline

S = input().strip()
Q = int(input())

sum_value = [[0 for _ in range(26)] for _ in range(len(S)+1)]

for i in range(1, len(S)+1):
    for j in range(26):
        sum_value[i][j] = sum_value[i-1][j]
    sum_value[i][ord(S[i-1])-97] += 1

for _ in range(Q):
    alpha, s, e = input().split()
    s, e = int(s), int(e)

    print(sum_value[e+1][ord(alpha)-97] - sum_value[s][ord(alpha)-97])
