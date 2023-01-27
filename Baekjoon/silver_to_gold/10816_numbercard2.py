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

# print(' '.join(str(mdi[k]) for k in mdi.keys()))
# 위 처럼 출력하면 출력 M에 동일한 숫자가 나올경우 여러번 출력을 못함

for data in mli:
    print(mdi[data], end=' ')
