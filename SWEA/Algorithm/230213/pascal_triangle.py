# 파스칼삼각형_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [[0 for i in range(N)] for i in range(N)]

    for j in range(N):
        for k in range(N):
            if k == 0:
                mat[j][k] = 1
            elif j != 0:
                mat[j][k] = mat[j-1][k-1] + mat[j-1][k]

    print(f'#{tc}')
    for v in mat:
        for i in range(len(v)):
            if v[i] != 0:
                print(v[i],end=' ')
        print('')


'''
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
 
    stack = []
    print(f'#{tc}')
    for _ in range(N):
        # 처음 스택이 비었으므로 1을 추가하고, 프린트 해주기
        if not stack:
            stack.append(1)
            print(*stack)
            continue
 
        # N이 2 이상인 경우 임시 list를 만들어서 파스칼의 삼각형 만들기
        temp_li = [stack[-1]]
        while stack:
            # 마지막 전까지, pop한 값과 stack의 top값을 더하면 원하는 값이 되므로 append
            if len(stack) > 1:
                temp_li.append(stack.pop()+stack[-1])
            # stack의 마지막값은 항상 1이므로 그냥 pop
            else:
                temp_li.append(stack.pop())
        stack = temp_li
        print(*stack)
'''


