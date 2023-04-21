# 9655_돌게임_Rockgame
import sys
input = sys.stdin.readline

N = int(input())
if N == 1 or N == 3:
    print('SK')
elif N == 2:
    print('CY')
else:
    if N % 4 == 0 or N % 4 == 2:
        print('CY')
    else:
        print('SK')

