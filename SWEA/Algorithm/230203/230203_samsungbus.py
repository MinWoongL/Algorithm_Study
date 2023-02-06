# 삼성시의버스노선_서울2반_이민웅

# 5000개의 버스 정류장, N개의 버스노선, i번째 버스노선(Ai 이상 Bi이하 정류장을 다니는 버스노선)

T = int(input())

for i in range(1, T+1):
    N = int(input())
    AB = []

    for _ in range(N):
        ab = list(map(int, input().split()))
        AB.append(ab)

    P = int(input())

    c_li = []
    for _ in range(P):
        c_li.append(int(input()))

    c_di = {}
    for v in c_li:
        c_di[v] = 0

    for value in AB:
        for j in range(value[0], value[1]+1):
            if j in c_di.keys():
                c_di[j] += 1

    print('#{}'.format(i), end=' ')
    for k in c_li:  # 키 값을 기준으로 출력하면 중복된 C를 출력할 수 없음
        print(c_di[k], end=' ')
    print('')



