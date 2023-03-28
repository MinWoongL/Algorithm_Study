# SWEA_baby-Gin

T = int(input())

for tc in range(1, T+1):

    n_li = list(map(int, input().split()))
    c1 = [0]*10
    c2 = [0]*10

    for i in range(2):
        c1[n_li[2*i]] += 1
        c2[n_li[2*i+1]] += 1

    ans = 0

    for i in range(4, len(n_li)):
        if i % 2 == 0:
            c1[n_li[i]] += 1
            if c1[n_li[i]] == 3:
                ans = 1
                break
            for j in range(8):
                if c1[j] >= 1 and c1[j+1] >= 1 and c1[j+2] >= 1:
                    ans = 1
                    break

        else:
            c2[n_li[i]] += 1
            if c2[n_li[i]] == 3:
                ans = 2
                break
            for j in range(8):
                if c2[j] >= 1 and c2[j+1] >= 1 and c2[j+2] >= 1:
                    ans = 2
                    break
        if ans != 0:
            break


    print(f'#{tc} {ans}')
