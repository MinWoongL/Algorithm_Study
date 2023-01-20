#  대표값 2

nli = []
for i in range(5):
    n = int(input())
    nli.append(n)

ave = int(sum(nli)/5)  # 자연수로 출력
nli.sort()
med = nli[2]

print(ave)
print(med)
