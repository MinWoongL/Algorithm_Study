# B_Lost permutation

T = int(input())

for tc in range(T):
    m, s = map(int, input().split())

    nli = list(map(int, input().split()))

    num = 1
    while s > 0:
        if num not in nli:
            nli.append(num)
            s = s - num
        num += 1

    nli.sort()

    if s != 0:
        print('No')
    else:
        check = True
        for i in range(len(nli)-1):
            if nli[i] != nli[i+1]-1:
                check = False
        if check:
            print('Yes')
        else:
            print('No')


