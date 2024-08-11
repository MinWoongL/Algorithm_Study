import sys
input = sys.stdin.readline

N, L = map(int, input().split())

mulseyo = list(map(int, input().split()))
mulseyo.sort()

cnt = 0
end = 0

for p in mulseyo:
    if p > end:
        cnt += 1
        end = p+L-1

print(cnt)