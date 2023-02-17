# SWEA 4408. 자기 방으로 돌아가기

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    room = [sorted(list(map(int, input().split()))) for _ in range(N)]
    room.sort()
    for room_num in room:
        if room_num[0] % 2:     # 앞쪽 방번호가 홀수면
            room_num[0] += 1
        if room_num[1] % 2:     # 뒤쪽 방번호가 홀수면
            room_num[1] += 1

    # print(room)     # (방 번호 낮은 것, 방 번호 높은 것)

    moved = [False] * N     # 학생의 이동 여부

    cnt = 0
    i = 0
    while False in moved:
        moved[i] = True     # i번 학생 이동
        # print(moved)
        for j in range(i + 1, N):       # i번 학생 이후 학생들 중

            if (room[i][1] < room[j][0]) and not moved[j]:      # 같이 이동할 수 있는 학생
                i = j       # 기준점 바꿔
                break
        # 같이 이동할 학생이 없어서 break 되지 않으면 1번의 이동 끝난 것
        else:
            cnt += 1
            for j in range(N):
                if not moved[j]:
                    i = j
                    break

    print(f'#{tc} {cnt}')