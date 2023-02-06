# 부분집합의 합_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())

    mat = [i for i in range(1, 13)]
    m = len(mat)

    subset_li = []
    for i in range(1<<m):
        s_set = []
        for j in range(m):
            if i & (1<<j):
                s_set.append(mat[j])
        if len(s_set) == n:
            subset_li.append(s_set)

    cnt = 0
    for v in subset_li:
        ans = 0
        for vv in v:
            ans += vv
        if ans == k:
            cnt +=1

    print(f'#{tc} {cnt}')