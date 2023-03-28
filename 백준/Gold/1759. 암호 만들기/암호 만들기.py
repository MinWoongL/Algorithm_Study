# 1759_암호만들기_password
import sys
input = sys.stdin.readline


def make_word(n):
    if len(ans) == L:
        cnt = 0
        for i in range(L):
            if ans[i] in vowels:
                cnt += 1
        if 0 < cnt < L-1:
            print(*ans, sep='')
        else:
            return

    for i in range(n, C):
        ans.append(c_li[i])
        make_word(i+1)
        ans.pop()


L, C = map(int, input().split())

c_li = list(map(str, input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

c_li.sort()
ans = []

make_word(0)