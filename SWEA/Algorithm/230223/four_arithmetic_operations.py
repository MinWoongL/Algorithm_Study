# 사칙연산_서울2반_이민웅

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


for tc in range(1, 11):
    N = int(input())
    heap = [[] for _ in range(2*N)]

    for _ in range(N):
        lst = list(map(str, input().split()))

        if lst[1].isdigit():
            heap[int(lst[0])].append(int(lst[1]))
        else:
            heap[int(lst[0])].append(lst[1])
            heap[int(lst[0])].append(int(lst[2]))
            heap[int(lst[0])].append(int(lst[3]))

    for j in range(N, 0, -1):
        if type(heap[j][0]) == str:
            if heap[j][0] == '+':
                heap[j] = [heap[heap[j][1]][0] + heap[heap[j][2]][0]]
            elif heap[j][0] == '-':
                heap[j] = [heap[heap[j][1]][0] - heap[heap[j][2]][0]]
            elif heap[j][0] == '*':
                heap[j] = [heap[heap[j][1]][0] * heap[heap[j][2]][0]]
            else:
                heap[j] = [heap[heap[j][1]][0] // heap[heap[j][2]][0]]

    print(f'#{tc} {heap[1][0]}')

