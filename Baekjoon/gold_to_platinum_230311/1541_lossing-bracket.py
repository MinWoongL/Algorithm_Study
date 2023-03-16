# 1541_잃어버린괄호_loosing-bracket
import sys

word = list(map(str, input().split('-')))

check = list(map(int, word[0].split('+')))
ans = sum(check)
if len(word) > 1:
    for i in range(1, len(word)):
        new = list(map(int, word[i].split('+')))
        n_sum = sum(new)
        ans -= n_sum
print(ans)
