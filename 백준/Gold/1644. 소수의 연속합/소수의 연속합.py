# 1644_소수의 연속합_a series of prime number
import sys
input = sys.stdin.readline

def make_prime_number(num):
    p_num = [True]*(num+1)

    s = 2
    while s**2 <= num:
        if p_num[s]:
            for i in range(s**2, num+1, s):
                p_num[i] = False
        s += 1
    rlt = [i for i in range(2, num+1) if p_num[i]]

    return rlt


N = int(input())

prime_lst = make_prime_number(N)

i, j, l = 0, 0, len(prime_lst)
tmp = 0
ans = 0
while j < l:
    if tmp < N:
        tmp += prime_lst[j]
        j += 1
    elif tmp > N:
        tmp -= prime_lst[i]
        i += 1
    else:
        ans += 1
        tmp += prime_lst[j]
        j += 1

while i < l and i <= j:
    if tmp == N:
        ans += 1
    tmp -= prime_lst[i]
    i += 1

print(ans)
