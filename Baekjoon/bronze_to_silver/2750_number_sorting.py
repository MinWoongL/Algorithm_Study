#  수 정렬하기

N = int(input())
nli = []

for i in range(N):
    n = int(input())
    nli.append(n)

nli.sort()

for v in nli:
    print(v)
