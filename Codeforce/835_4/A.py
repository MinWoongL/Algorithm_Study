# A_Medium Number

T = int(input())

for tc in range(T):
    nli = list(map(int, input().split()))
    nli.sort()
    print(nli[1])



