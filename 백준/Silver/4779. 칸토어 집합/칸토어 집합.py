# 4779_칸토어 집합
import sys
input = sys.stdin.readline

def func(str):
    if len(str) == 1:
        return str

    if "-" in str:
        l = len(str)//3

        ans = ""
        ans += func(str[:l])
        ans += func(" "*l)
        ans += func(str[:l])
    else:
        ans = str

    return ans

while True:
    try:
        N = int(input())
        start = '-' * (3 ** N)
        print(func(start))
    except:
        break