# 당근 포장하기

# 대, 중, 소 상자
# N//2 초과 ㄴㄴ
# 상자 별 당근 수 차이 최소
# 같은크기는 같은 상자에
# 3<=N<=1000, 1<=Ci<=30

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    carrot_li = list(map(int, input().split()))
    carrot_li.sort()

    carrot_set = set(carrot_li)
    carrot_dict = {}
    ans = 0
    b1 = b2 = b3 = 0
    for v in carrot_li:
        if v not in carrot_dict.keys():
            carrot_dict[v] = 1
        else:
            carrot_dict[v] += 1

    for c in carrot_set:
        if carrot_dict[c] > N//2:
            ans = -1
            break
        else:
            if b1 <= b2 and b1 <= b3:
                b1 += carrot_dict[c]
            elif b2 <= b1 and b2 <= b3:
                b2 += carrot_dict[c]
            elif b3 <= b1 and b3 <= b2:
                b3 += carrot_dict[c]

    if ans != -1:
        if b1 == 0 or b2 == 0 or b3 == 0:
            ans = -1
        else:
            ans = max(b1, b2, b3) - min(b1, b2, b3)

    print(carrot_dict)

    print(f'#{tc} {ans}')
