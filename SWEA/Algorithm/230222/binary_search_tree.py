# 이진탐색_서울2반_이민웅

def makeTree(start, N):
    global bt
    if start <= N:
        makeTree(2*start, N)
        bt.append(start)
        makeTree(2*start+1, N)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    bt = []

    makeTree(1, N)
    # print(bt)
    ans = 0
    ans2 = 0
    for i in range(len(bt)):
        if bt[i] == 1:
            ans = i
    for j in range(len(bt)):
        if bt[j] == N//2:
            ans2 = j

    print(f'#{tc} {ans+1} {ans2+1}')








