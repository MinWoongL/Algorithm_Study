import sys
input = sys.stdin.readline

text = input().strip()

if text == text[::-1]:
    print(1)
else:
    print(0)