# 2775_부녀회장이 될테야_apartment

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    ans = []
    for j in range(1, n+1):
        ans.append(j)

    for num in range(k):
        for unit in range(1, n):
            ans[unit] += ans[unit-1]

    print(ans[-1])