import sys
# 0
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    # 1
    # lst = [list(map(int, input().split())) for _ in range(N)]
    # for _ in range(N):
    #     lst.append(list(map(int, input().split())))
    lst = [0]*N
    for _ in range(N):
        a, b = map(int, input().split())
        lst[a-1] = [a, b]

    # 첫번째 점수로 정렬
    # lst.sort()
    li = [lst[0]]
    cnt = 1

    i = 0
    j = 1
    while True:
        # 2
        if lst[i][1] == 1 or j == N:
            break
        if lst[i][1] < lst[j][1]:
            j += 1
        else:
            # 3
            # li.append(lst[j])
            cnt += 1
            i = j
            j += 1
    # print(len(li))
    print(cnt)

