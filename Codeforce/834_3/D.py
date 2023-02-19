# D_Make it Round

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    # print(str(n)[-1])
    if int(str(n)[-1]) == 0:
        print(0)

    elif int(str(n)[-1])%2 == 0:
        if m < 5:
            print(n*m)
        else:
            check = m//5
            m = 5*check
            print(n*m)

    elif int(str(n)[-1]) == 5:
        if m < 2:
            print(n*m)
        elif m > 10:
            check = m//10
            m = 10*check
            print(n*m)
        else:
            check = m//2
            m = 2*check
            print(n*m)
    else:
        if m < 10:
            print(n*m)
        else:
            check = m//10
            m = 10*check
            print(n*m)



