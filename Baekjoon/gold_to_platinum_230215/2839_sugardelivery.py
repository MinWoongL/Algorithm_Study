# 2839_설탕배달_sugar-delivery

N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    cnt = 0
    while N > 0:
        N -= 3
        cnt += 1
        if N % 5 == 0:
            cnt += N//5
            break
        elif N == 1 or N == 2:
            cnt = -1
            break
    print(cnt)


