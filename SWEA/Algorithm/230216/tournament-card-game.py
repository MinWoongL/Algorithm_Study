# 토너먼트카드게임_서울2반_이민웅

def rsp(li):
    if len(li) == 1:
        return li
    else:
        mid = ((len(li)+1)//2)
        left = rsp(li[:mid])
        right = rsp(li[mid:])

        if left[0][0] == right[0][0]:
            return left
        elif left[0][0] == 3:
            if right[0][0] == 1:
                return right
            else:
                return left
        elif left[0][0] == 1:
            if right[0][0] == 2:
                return right
            else:
                return left
        else:
            if left[0][0] == 2:
                if right[0][0] == 3:
                    return right
                else:
                    return left


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nli = list(map(int, input().split()))
    rsp_li = []
    for i in range(1, N+1):
        rsp_li.append([nli[i-1], i])
    # print(rsp_li)
    ans = rsp(rsp_li)
    print(f'#{tc} {ans[0][1]}')
