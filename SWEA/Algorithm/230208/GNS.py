# GNS_서울2반_이민웅

T = int(input())
num_li = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    tnum, N = map(str, input().split())
    N = int(N)

    num_di = {}
    ans_li = []
    for v in num_li:
        num_di[v] = 0

    test_list = list(map(str, input().split()))
    for word in test_list:
        num_di[word] += 1

    for num in num_li:
        for i in range(num_di[num]):
            ans_li.append(num)
    print('{}'.format(tnum))
    print(*ans_li)

    for key, val in num_di.items():
        print((key+' ')*val, end="")
    print()



