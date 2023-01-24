n = int(input())
p_li = []
sort_p_li = []  # 필요없음
rank_li = []
for i in range(n):
    data = list(map(int, input().split()))
    p_li.append(data)

sort_p_li = sorted(p_li, key=lambda x: x[1])  # p_li.sort 로 하면 p_li만 정렬이 되고 sort_p_li에 복사가 되지 않음
# 정렬 할 필요 없었음
for i in range(n):
    rank = 1
    for j in range(n):  # 전체 다 비교해보면 등수를 알 수 있음.
        if p_li[i][0] < p_li[j][0] and p_li[i][1] < p_li[j][1]:
            rank += 1
        else:
            pass
    rank_li.append(rank)

for v in rank_li:
    print(v,end=' ')