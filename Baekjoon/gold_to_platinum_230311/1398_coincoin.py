# 1398_동전문제_coincoin
# 31~34, 41~44
T = int(input())

coin = [1, 10, 25]
for tc in range(T):
    price = int(input())
    ans = 0
    while price > 0:
        check = price % 100
        cnt = 0
        if 30 <= check <= 34 or 40 <= check <= 44:
            idx = 1
            while check != 0:
                if check - coin[idx] >= 0:
                    check -= coin[idx]
                    cnt += 1
                else:
                    idx -= 1
        elif 55 <= check <= 59 or 65 <= check <= 69:
            cnt = 1
            idx = 1
            check = check - 25
            while check != 0:
                if check - coin[idx] >= 0:
                    check -= coin[idx]
                    cnt += 1
                else:
                    idx -= 1
        elif 80 <= check <= 84 or 90 <= check <= 94:
            cnt = 2
            idx = 1
            check = check - 50
            while check != 0:
                if check - coin[idx] >= 0:
                    check -= coin[idx]
                    cnt += 1
                else:
                    idx -= 1
        else:
            idx = 2
            while check != 0:
                if check - coin[idx] >= 0:
                    check -= coin[idx]
                    cnt += 1
                else:
                    idx -= 1
        price = price//100
        ans += cnt

    print(ans)



