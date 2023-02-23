# 이진 힙_서울2반_이민웅

def enq(n):
    global last

    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]:

        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]*(N+1)
    last = 0
    nli = list(map(int, input().split()))

    for v in range(N):
        enq(nli[v])
    # print(nli)
    print(heap)

    ans = 0
    idx = N//2
    while idx > 0:
        ans += heap[idx]
        idx //= 2
    print(f'#{tc} {ans}')


