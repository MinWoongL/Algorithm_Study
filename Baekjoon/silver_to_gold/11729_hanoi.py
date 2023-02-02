# 11729_하노이 탑 이동순서_Hanoi

def hanoi(n, li, k):
    if k == 1:
        o = 1
        t = 2
        th = 3
        if n == 2:
            li.append((o, t))
            li.append((o, th))
            li.append((t, th))
            return li
        else:
            if n % 2 == 0:

                return hanoi(n-1, li, k)



def cnt(n):
    if n == 1:
        return 1
    else:
        return cnt(n - 1) + 2**(n-1)


# 12 13 23, 13 12 32 13 21 23 13, 12 13 23 12 31 32 12 13 23 21 31 23 12 13 23
N = int(input())

move_li = []

if N%2 == 1:
    o_e = 0
else:
    o_e = 1
count = cnt(N)
print(count)
print(hanoi(N, move_li))
