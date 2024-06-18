# 9324_진짜메시지_Real message
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    text = input().strip()

    checker = {}
    idx = 0
    ans = "OK"
    while idx < len(text):
        tmp = text[idx]
        if tmp in checker.keys():
            checker[tmp] += 1
            if checker[tmp] == 3:
                if idx + 1 >= len(text) or text[idx+1] != tmp:
                    ans = "FAKE"
                    break
                else:
                    checker[tmp] = 0
                    idx += 1

        else:
            checker[tmp] = 1
        idx += 1

    print(ans)