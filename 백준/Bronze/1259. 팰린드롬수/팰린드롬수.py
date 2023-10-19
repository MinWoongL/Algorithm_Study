# 1259_팰린드롬수_pallindrome-number
import sys
sys = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break
    else:
        if s == s[::-1]:
            if s[-1] != '0':
                print('yes')
            else:
                print('no')
        else:
            print('no')