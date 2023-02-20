# 회전_서울2반_이민웅

def isEmptycQ():
    return front == rear

def isFullcQ():
    return (rear+1) % len(cQ) == front

def enQueuecQ(item):
    global rear
    if isFullcQ():
        print("Queue_Full")
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueuecQ():
    global front
    if isEmptycQ():
        print("Queue_Empty")
    else:
        front = (front+1) % len(cQ)
        return cQ[front]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nli = list(map(int, input().split()))

    cQ = [0]*(N+1)
    front = rear = 0

    for v in nli:
        enQueuecQ(v)

    for i in range(M):
        num = deQueuecQ()
        enQueuecQ(num)

    print(f'#{tc} {cQ[front+1]}')



