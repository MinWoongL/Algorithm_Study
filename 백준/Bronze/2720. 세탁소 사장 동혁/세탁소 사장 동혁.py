T = int(input())
check = [25, 10, 5, 1]

for tc in range(T):
    dollar = int(input())

    ans = []

    for i in range(4):
        tmp = 0
        while True:
            if dollar < check[i]:
                ans.append(tmp)
                break
            else:
                dollar -= check[i]
                tmp += 1

    print(*ans)
