# C. Premutation

# 원래 순열의 모습 찾기
import sys
import collections

t = int(input())

for i in range(t):
    n = int(input())
    ans = []
    mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    fli = []
    lli = []
    for j in range(n):
        fli.append(mat[j][0])
        lli.append(mat[j][-1])
    n1 = collections.Counter(fli).most_common(1)[0][0]
    n_last = collections.Counter(lli).most_common(1)[0][0]

    ans.append(n1)

    for v in mat:
        if n1 in v:
            v.remove(n1)
        if n_last in v:
            v.remove(n_last)

    mn = 0
    idx = 0

    for i in range(len(mat)):
        if len(mat[i]) >= mn:
            idx = i
            mn = len(mat[i])

    for v in mat[idx]:
        ans.append(v)
    ans.append(n_last)
    for v in ans:
        print(v, end=' ')
    print('')


