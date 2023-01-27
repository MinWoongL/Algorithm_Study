# 10816_숫자카드2_numbercard2

N = int(input())
nli = list(map(int, input().split()))

M = int(input())
mli = list(map(int, input().split()))
mdi = {}

for v in mli:
    mdi[v] = 0


for v in nli:
    if v in mdi.keys():
        mdi[v] += 1

nnli = []
for k in mdi.keys():
    nnli.append(mdi[k])

# for i in range(len(nnli)):
#     if i != (len(nnli)-1):
#         print(nnli[i], end=' ')
#     else:
#         print(nnli[i], end='')

# print(' '.join(str(mdi[k]) for k in mdi.keys()))

for data in mli:
    print(mdi[data], end=' ')