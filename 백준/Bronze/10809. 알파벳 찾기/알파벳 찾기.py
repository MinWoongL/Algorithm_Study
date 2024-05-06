import sys
input = sys.stdin.readline

text = input().strip()

alpha = {}

for i in range(ord("a"), ord("z")+1):
    alpha[chr(i)] = -1

for i in range(len(text)):
    if alpha[text[i]] == -1:
        alpha[text[i]] = i

for i in range(ord("a"), ord("z")+1):
    print(alpha[chr(i)], end=" ")