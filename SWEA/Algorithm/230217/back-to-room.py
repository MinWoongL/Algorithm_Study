# 4408_자기 방으로 돌아가기_back-to-room

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    corridor = [0] * 201
    for _ in range(N):
        s, g = map(int, input().split())
        if g < s:
            g, s = s, g
        s -= 1
        g -= 1
        s //= 2
        g //= 2
        for i in range(s, g+1):
            corridor[i] += 1

    max_value = 0
    # print(corridor)
    for v in corridor:
        if v > max_value:
            max_value = v
    print(f'#{tc} {max_value}')


# import heapq
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     student_li = []
#     for _ in range(N):
#         s, g = map(int, input().split())
#         if g < s:
#             g, s = s, g
#             s -= 1
#             g -= 1
#         student_li.append([s, g])
#     student_li.sort(key=lambda x: x[0])
#     # print(student_li)
#     time = []
#     heapq.heappush(time, student_li[0][1])
#
#     for i in range(1, N):
#         if student_li[i][0] < time[0]:
#             heapq.heappush(time, student_li[i][1])
#         else:
#             heapq.heappop(time)
#             heapq.heappush(time, student_li[i][1])
#
#     ans = len(time)
#
#     print(f'#{tc} {ans}')