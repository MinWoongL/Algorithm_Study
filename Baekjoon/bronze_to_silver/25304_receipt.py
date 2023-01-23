# 25304_영수증

cost = int(input())  # 영수증 금액

num_of_p = int(input())

s = 0  # 물건가격의 합
for i in range(num_of_p):
    pn = list(map(int, input().split()))
    sumofpn = pn[0]*pn[1]
    s += sumofpn

if s == cost:
    print('Yes')
else:
    print('No')
