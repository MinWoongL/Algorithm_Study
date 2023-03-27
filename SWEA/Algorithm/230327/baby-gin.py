# 서울2반_baby-gin

def perm2(lst, n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for i in lst:
            result.append([i])
    elif n > 1:
        for i in range(len(lst)):
            ans = [i for i in lst]
            ans.remove(lst[i])
            for p in perm2(ans, n-1):
                result.append([lst[i]]+p)

    return result


def baby_gin(lst):
    n = len(lst)
    check = 0
    for i in range(n-1):
        if lst[i] + 1 == lst[i+1]:
            continue
        else:
            break
    else:
        check = 1

    for i in range(n-1):
        if lst[i] == lst[i+1]:
            continue
        else:
            break
    else:
        check = 1

    return check


T = int(input())

for tc in range(1, T+1):

    baby = list(map(int, input()))
    n_li = [i for i in range(1, 7)]

    a = perm2(n_li, 3)
    ans = 'Lose'
    for v in a:
        n1 = []
        n2 = []
        b_check = 0
        for i in v:
            n1.append(baby[i-1])
        for i in range(1, 7):
            if i not in v:
                n2.append(baby[i-1])
        n1.sort()
        n2.sort()

        b_check += baby_gin(n1)
        b_check += baby_gin(n2)
        if b_check == 2:
            ans = 'Baby Gin'
            break

    print(f'#{tc} {ans}')
