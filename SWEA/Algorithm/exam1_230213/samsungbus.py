
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    AB = []

    for _ in range(N):
        ab = list(map(int, input().split()))
        AB.append(ab)

    P = int(input())

    c_li = []
    for _ in range(P):
        c_li.append(int(input()))

    c_di = {}
    for v in c_li:
        c_di[v] = 0

    for value in AB:
        for j in range(value[0],value[1]+1):
            if j in c_di.keys():
                c_di[j] += 1

    print('#{}'.format(tc), end=' ')
    for li_value in c_li:
        print(c_di[li_value], end=' ')
    print('')









