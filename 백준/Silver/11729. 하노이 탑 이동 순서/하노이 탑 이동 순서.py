# 11729_하노이 탑 이동순서_Hanoi

def hanoi(n, li, a, b, c):
    sub_li = []
    if n == 1:
        li.append([a, c])
        return li
    elif n == 2:
        li.append([a, b])
        li.append([a, c])
        li.append([b, c])
        return li

    ans_li = []
    ans = hanoi(n-1, li, a, c, b)
    for v in ans:
        ans_li.append(v)

    ans_li.append([a, c])

    ans2 = hanoi(n-1, sub_li, b, a, c)
    for v1 in ans2:
        ans_li.append(v1)

    return ans_li


def cnt(n):
    if n == 1:
        return 1
    else:
        return cnt(n - 1) + 2**(n-1)


# 12 13 23, 13 12 32 13 21 23 13, 12 13 23 12 31 32 12 13 23 21 31 23 12 13 23
N = int(input())

move_li = []
count = cnt(N)

print(count)
last_li = hanoi(N, move_li, 1, 2, 3)
for v in last_li:
    print(*v)

