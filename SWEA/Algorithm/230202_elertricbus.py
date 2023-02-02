# 전기버스_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    m_li = list(map(int, input().split()))

    stop_checker = True
    cnt = 0
    cur = 0
    while cur < N:
        for i in range(K+cur, cur, -1):
            if cur + K >= N:
                cur = N
                break

            if i in m_li:
                cur = i
                cnt += 1
                break

            if i == cur + 1:
                cnt = 0
                stop_checker = False
                break

        if stop_checker is False:
            break

    print('#{} {}'.format(tc, cnt))




# T = int(input())
#
# for test_case in range(1, T + 1):
#
#     K, N, M = map(int, input().split())
#     M_li = list(map(int, input().split()))
#     position = [0]  # 방문 충전소 목록 인덱스 -1이 현재 위치
#     TF = True
#     cnt = 0  # 충전 횟수 카운트
#     # 현재 버스의 위치 A_i 내맘대로
#     while position[-1] < N:  # 버스의 현재 위치가 N보다 작은동안 실행
#
#         for i in range(K + position[-1], position[-1], -1):  # 충전 횟수 최소 -> 현재 위치부터 K만큼 떨어진 곳부터 역순 탐색
#             if N - position[-1] <= K:  # 다만 K번 내로 도착지에 도착 가능하다면 도착시키고 종료
#                 position.append(N)
#                 break
#
#             if i in M_li:  # 거꾸로 탐색하면서 i가 리스트 안에 있으면 위치 갱신하고 그 즉시 브레이크
#
#                 position.append(i)  # 현재 포지션 저장
#                 cnt += 1  # 충전 횟수 추가
#                 break
#             if i == position[-1] + 1:  # for문을 다 돌았는데도 도착이나 충전을 못했다면 더이상 이동 불가능하므로 cnt 0으로 초기화하고 break
#                 cnt = 0
#                 TF = False
#                 break
#         if TF == False:
#             break
#     print(f'#{test_case} {cnt}')

