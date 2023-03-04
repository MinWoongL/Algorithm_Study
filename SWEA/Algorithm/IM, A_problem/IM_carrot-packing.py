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

    carrot_dict = {}
    ans = 10000000
    b1 = b2 = b3 = 0
    for v in carrot_li:
        if v not in carrot_dict.keys():
            carrot_dict[v] = 1
        else:
            carrot_dict[v] += 1
    carrot_num_li = []
    for key in carrot_dict.keys():
        if carrot_dict[key] > N // 2:
            ans = -1
            break
        else:
            carrot_num_li.append(carrot_dict[key])

    if ans != -1:
        for i in range(len(carrot_num_li) - 2):
            for j in range(i + 1, len(carrot_num_li) - 1):
                b1 = sum(carrot_num_li[:i+1])
                b2 = sum(carrot_num_li[i+1:j+1])
                b3 = sum(carrot_num_li[j+1:])
                if b1 > N//2 or b2 > N//2 or b3 > N//2:
                    continue
                else:
                    if ans > (max(b1,b2,b3) - min(b1,b2,b3)):
                        ans = (max(b1,b2,b3) - min(b1,b2,b3))

    if ans == 10000000:
        ans = -1
    print(f'#{tc} {ans}')