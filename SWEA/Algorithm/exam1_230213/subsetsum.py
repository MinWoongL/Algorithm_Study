
def comb(li, n):
    result = []
    if n > len(li):
        return li
    if n == 1:
        for i in li:
            result.append([i])
    else:
        for i in range(len(li)-n+1):
            for j in comb(li[i+1:], n-1):
                result.append([li[i]] + j)

    return result


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nli = [i for i in range(1,13)]

    ans_li = comb(nli, n)
    sum_value = 0
    cnt = 0
    for v in ans_li:
        for value in v:
            sum_value += value
        if sum_value == m:
            cnt += 1
        sum_value = 0

    print(f'#{tc} {cnt}')

    # subset = []
    # for i in range(1<<12):
    #     s_set = []
    #     for j in range(12):
    #         if i & (1<<j):
    #             s_set.append(nli[j])
    #     if len(s_set) == n:
    #         subset.append(s_set)
