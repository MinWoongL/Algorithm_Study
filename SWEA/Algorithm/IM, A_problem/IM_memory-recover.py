# 원재의 메모리 복구하기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    memory = list(input())
    cnt = 0
    current = 0
    for i in range(len(memory)):
        if int(memory[i]) != current:
            cnt += 1
            if current == 0:
                current = 1
            else:
                current = 0
    print(f'#{tc} {cnt}')

