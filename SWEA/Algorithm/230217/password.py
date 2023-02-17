# 1234_비밀번호_서울_2반_이민웅

# T = int(input())

for tc in range(1, 11):
    n, word = map(str, input().split())

    stack = []
    for v in word:
        if not stack:
            stack.append(v)
        else:
            if stack[-1] == v:
                stack.pop()
            else:
                stack.append(v)
    print(f'#{tc}',end=' ')
    print(*stack, sep='')