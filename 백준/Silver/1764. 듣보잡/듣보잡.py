# 1764_듣보잡

import sys

n, m = map(int, input().split())
emedi = {}
qhli = []
count = 0
emeqhli = []
for i in range(n):
    s = sys.stdin.readline().strip()
    emedi[s] = 0

for j in range(m):
    s = sys.stdin.readline().strip()
    qhli.append(s)

for v in qhli:
    if v in emedi.keys():
        count += 1
        emeqhli.append(v)
emeqhli.sort()
print(count)
for value in emeqhli:
    print(value)

