# E_Humanoid

T = int(input())

for tc in range(T):
    n, h = map(int, input().split())

    green = 2
    blue = 1

    ast_li = list(map(int, input().split()))

    ast_li.sort()
    idx = 0
    cnt = 0
    while True:
        if idx <= n-1:
            if ast_li[idx] < h:
                h += ast_li[idx]//2
                idx += 1
                cnt += 1
            elif blue != 0 and h*3 > ast_li[idx]:
                blue -= 1
                h *= 3
            elif green != 0 and h*2 > ast_li[idx]:
                green -= 1
                h *= 2
            elif green == 2 and h*4 > ast_li[idx]:
                green -= 1
                h *= 4
            elif green != 0 and blue != 0 and h*6 > ast_li[idx]:
                green -= 1
                blue -= 1
                h *= 6
            else:
                break
        else:
            break
    print(cnt)






