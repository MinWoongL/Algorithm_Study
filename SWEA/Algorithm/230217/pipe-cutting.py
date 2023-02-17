# 5432_쇠막대기 자르기_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    stack = []
    cnt = 0

    bracket = str(input())

    before = ''

    for b in bracket:
        if not stack:
            stack.append(b)
        else:
            if b == '(':
                stack.append(b)
            elif b == ')' and before == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
        before = b

    print(f'#{tc} {cnt}')