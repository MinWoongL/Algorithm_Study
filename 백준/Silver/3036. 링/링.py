# 3036_링_Ring

def GCD(a, b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a


N = int(input())

r_li = list(map(int, input().split()))
r1 = r_li[0]

for v in range(1, len(r_li)):
    ans = GCD(r1, r_li[v])

    print(f'{r1//ans}/{r_li[v]//ans}')
