import sys

T = int(input())

for tc in range(T):
    N, word = input().split()
    N = int(N)
    ans = ''
    for w in word:
        for i in range(N):
            ans += w

    print(ans)