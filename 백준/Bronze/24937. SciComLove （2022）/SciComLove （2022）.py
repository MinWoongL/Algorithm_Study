import sys
input = sys.stdin.readline

N = int(input())

text = "SciComLove"

N = N % 10

ans = text[N:] + text[:N]
print(ans)