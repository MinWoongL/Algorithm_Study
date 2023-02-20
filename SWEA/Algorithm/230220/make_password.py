# 암호생성기_서울2반_이민웅

for tc in range(1, 11):
    T = int(input())
    c_q = list(map(int, input().split()))
    front = rear = 0

    maker = 1
    while True:
        if c_q[rear%8] - maker <= 0:
            c_q[rear%8] = 0
            break
        else:
            c_q[rear%8] = c_q[rear%8] - maker
            maker = maker + 1
            if maker == 6:
                maker = 1
            front = (front+1)%8
            rear = (rear+1)%8
    if front != 7:
        ans = c_q[front+1:] + c_q[:front+1]
    else:
        ans = c_q[:front]
    print(f'#{T} ', end='')
    print(*ans)


