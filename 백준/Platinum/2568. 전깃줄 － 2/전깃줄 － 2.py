# 2568_전깃줄2_Electric wire2
import sys
input = sys.stdin.readline


def bs(lst, num):
    l, r = 0, len(lst)-1
    while l <= r:
        mid = (l+r)//2

        if lst[mid][0] <= num:
            l = mid + 1
        else:
            r = mid - 1
    return l



N = int(input())

wires = []

for _ in range(N):
    w1, w2 = map(int, input().split())
    wires.append([w1, w2])

wires.sort(key=lambda x: x[1])

ws = [(wires[0][0], 0)]

parent = [-1]*N

for i in range(1, N):
    tmp_w = wires[i][0]
    w_idx = bs(ws, tmp_w)

    if w_idx == len(ws):
        ws.append((tmp_w, i))
    else:
        ws[w_idx] = (tmp_w, i)

    if w_idx > 0:
        parent[i] = ws[w_idx-1][1]
    else:
        parent[i] = -1

lis = []
idx_check = ws[-1][1]

while idx_check != -1:
    lis.append(idx_check)
    idx_check = parent[idx_check]

ans = []
for i in range(N):
    if i not in lis:
        ans.append(wires[i][0])

ans.sort()

print(N-len(ws))
for v in ans:
    print(v)
