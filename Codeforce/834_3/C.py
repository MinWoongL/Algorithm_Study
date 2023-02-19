# C_Thermostat

T = int(input())

for tc in range(T):
    l, r, x = map(int, input().split())

    a, b = map(int, input().split())
    cnt = 0

    if a != b:
        if abs(b - a) >= x:
            print(1)
        elif b - l >= x and r - b >= x:
            if a - l >= x or r - a >= x:
                print(2)
            else:
                print(-1)
        elif b - l >= x:
            if a - l >= x:
                print(2)
            elif r - a >= x:
                print(3)
            else:
                print(-1)
        elif r - b >= x:
            if r - a >= x:
                print(2)
            elif a - l >= x:
                print(3)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(0)





