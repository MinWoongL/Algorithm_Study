# 진기의최고급붕어빵_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    n_li = list(map(int, input().split()))
    n_li.sort()

    boong = 0
    # 0초에 오는 손님도 걸러야해서 -1 부터 시작
    time = -1
    idx = 0
    ans = 'Possible'
    for i in range(0, n_li[-1]+1):
        time += 1
        if time == M:
            boong += K
            time = 0
        if i == n_li[idx]:
            # idx < len(n_li) 조건을 뒤에 두면 값이 1개인경우를 못거름
            while idx < len(n_li) and i == n_li[idx]:
                if boong != 0:
                    boong -= 1
                    idx += 1
                else:
                    ans = 'Impossible'
                    break
        if ans == 'Impossible':
            break

    print(f'#{tc} {ans}')
