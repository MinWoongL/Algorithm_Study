# 4153_직각삼각형_right-triangle
import sys

check = True
while check:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        check = False
    else:
        # 세가지 경우 모드 체크해줘야 정답
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print('right')
        else:
            print('wrong')

