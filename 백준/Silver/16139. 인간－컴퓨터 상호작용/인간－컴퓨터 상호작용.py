# 16139_인간-컴퓨터상호작용_Human-computer interaction
import sys
input = sys.stdin.readline

S = input()
Q = int(input())

for _ in range(Q):
    alpha, s, e = input().split()
    s, e = int(s), int(e)
    # print(alpha, s, e)
    print(S[s:e+1].count(alpha))
