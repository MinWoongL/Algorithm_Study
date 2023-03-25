import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(input())
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

    i = 0
    j = 1
    while True:
        if j == N or lst[i][1] == 1:
            break
        if lst[i][1] < lst[j][1]:
            j += 1
        else:
            li.append(lst[j])
            i = j
            j += 1
    print(len(li))

