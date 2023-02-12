
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    n_di = {2:0, 3:0, 5:0, 7:0, 11:0}
    idx = 2
    while N != 1:
        if N % idx == 0:
            n_di[idx] += 1
            N = N//idx
        else:
            idx += 1
    print(f'#{tc}', end=' ')
    for key, value in n_di.items():
        print(value, end=' ')
    print('')







