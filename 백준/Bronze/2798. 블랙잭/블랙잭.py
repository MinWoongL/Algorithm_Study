nm = list(map(int, input().split()))  # 숫자개수와 수 제한(M) 입력
M = nm[1]

nli = list(map(int, input().split()))
ans = 0
ans_li = []

for i in range(nm[0]):
    for j in range(i + 1, nm[0]):  # 겹치지 않게 2번째 숫자를 받기 위해 i+1 ~ 로 인덱싱
        for k in range(j + 1, nm[0]):  # 겹치지 않게 3번째 숫자를 받기 위해 j+1 ~ 로 인덱싱
            if nli[i] + nli[j] + nli[k] <= M:
                ans_li.append(nli[i] + nli[j] + nli[k])
            else:
                pass

ans_li.sort()  # 오름차순 정렬
print(ans_li[-1])  # 마지막 값 출력