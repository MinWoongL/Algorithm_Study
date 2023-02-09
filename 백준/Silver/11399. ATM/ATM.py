# 11399_ATM

N = int(input())

nli = list(map(int, input().split()))

nli.sort()
# print(nli)

value_sum = 0
now_sum = 0
for v in nli:
    now_sum += v
    value_sum += now_sum

print(value_sum)
