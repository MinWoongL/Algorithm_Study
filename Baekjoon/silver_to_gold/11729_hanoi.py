# 11729_하노이 탑 이동순서_Hanoi

def hanoi(n, li):
    if n == 1:
        return li.append((1, 3))
    elif n%2 == 1:
        pass


def cnt(n):
    if n == 1:
        return 1
    else:
        return cnt(n - 1) + 2**(n-1)


N = int(input())

move_li = []

count = cnt(N)
hanoi(N, move_li)
print(count)
