# 피자굽기_서울2반_이민웅

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza_li = list(zip(list(map(int, input().split())), list(i for i in range(1, M+1))))

    c_q = [(0, 0)]*N
    front = rear = 0
    pizza_in_fire = 0
    while pizza_li or pizza_in_fire > 1:
        if pizza_li:
            if pizza_in_fire < N:
                c_q[rear-1] = pizza_li.pop(0)
                pizza_in_fire += 1
        if c_q[front][0] != 0 and c_q[front][0] // 2 == 0:
            pizza_in_fire -= 1
            c_q[front] = (0, 0)
        else:
            c_q[rear] = (c_q[front][0] // 2, c_q[front][1])
        front = (front+1)%N
        rear = (rear+1)%N
    ans = 0
    for v in c_q:
        if v[0] != 0:
            ans = v[1]

    print(f'#{tc} {ans}')
