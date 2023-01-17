def hansu(n):
    count = 0
    for i in range(1, n+1):
        li = list(map(int, str(i)))
        if i < 100:
            count = i
        elif i <= 110:
            count = 99
        elif li[0]-li[1] == li[1]-li[2]:
            count += 1
    print(count)


n = int(input())


hansu(n)