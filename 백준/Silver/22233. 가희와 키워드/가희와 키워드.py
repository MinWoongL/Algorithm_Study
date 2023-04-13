# 22233_가희와키워드_GaheeKeyword
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keyword = {}
for i in range(N):
    keyword[input().strip()] = 1

for i in range(M):
    text = list(map(str, input().rstrip().split(',')))
    for v in text:
        if v in keyword:
            keyword.pop(v)
    print(len(keyword))

