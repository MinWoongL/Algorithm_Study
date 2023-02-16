# 배열최소합_서울2반_이민웅
# 스택메모리제한 -> 순열 경우의 수를 리스트에 저장하고 비교하면 안됌.
def perm(i, k, s):
    global min_value
    if i == k:
        s = 0
        for i in range(len(p_li)):
            s += mat[i][p_li[i]]
        if min_value > s:
            min_value = s
        return
    elif s >= min_value:  # 경우의 수를 줄여서 시간을 줄이는게 중요
        return
    else:
        for j in range(i, k):
            p_li[i], p_li[j] = p_li[j], p_li[i]
            perm(i+1, k, s+mat[i][p_li[i]])
            p_li[i], p_li[j] = p_li[j], p_li[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]
    p_li = [i for i in range(N)]

    min_value = 10 * N
    s = 0
    perm(0, N, s)

    print(f'#{tc} {min_value}')




T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]
    p_li = [i for i in range(N)]
    # ans_li = perm2(p_li, N)
    min_value = 10 * N
    perm(0, N)


    # for v in ans:
    #     s = 0
    #     for i in range(N):
    #         s += mat[i][v[i]]
    #     if s < min_value:
    #         min_value = s
    print(f'#{tc} {min_value}')

