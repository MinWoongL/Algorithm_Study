# G_Restore the permutation

T = int(input())

for tc in range(T):
    N = int(input())
    nli = list(map(int, input().split()))

    new_li = sorted(nli)
    p_li = []
    num = 1
    idx = 0
    print(nli)
    print(new_li)
    while idx <= len(nli)-1:
        if num < new_li[idx] and num not in p_li and num not in nli:
            p_li.append(num)
            p_li.append(nli[idx])
            num += 1
            idx += 1
        elif num < new_li[-1]:
            num += 1
        else:
            break
    print(p_li)
    if len(p_li) == N:
        print(*p_li)
    else:
        print(-1)

