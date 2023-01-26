# 14425_문자열집합_word

N, M = map(int, input().split())

sli = {}
count = 0
for i in range(N):
    s = input()
    sli[s] = 0

for j in range(M):
    s = input()
    if s in sli.keys():
        count += 1

print(count)