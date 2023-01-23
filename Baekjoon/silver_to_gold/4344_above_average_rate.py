# 4344_평균은넘겠지 : 나는 평균을 넘을까?

T = int(input())

for i in range(T):
    nli = list(map(int, input().split()))
    count = 0
    n = nli[0]
    nli.pop(0)
    ave = sum(nli) / len(nli)
    for value in nli:
        if value > ave:
            count += 1
    rate = count/n * 100
    # print("{}%".format((round(rate, 3))))  # 출력을 더 쉽고 깔끔하게 하면 좋을것 같다 -> 40.0 으로 출력되서 틀림
    print(f'{rate:.3f}%')  # 40.000% 로 출력 가능
