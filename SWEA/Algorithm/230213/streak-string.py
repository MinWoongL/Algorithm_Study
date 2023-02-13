# 반복문자 지우기

T = int(input())

for tc in range(1, T+1):
    sentence = str(input())
    stack = []

    for v in sentence:
        if not stack:
            stack.append(v)
        else:
            if stack[-1] == v:
                stack.pop()
            else:
                stack.append(v)

    ans = len(stack)

    print(f'#{tc} {ans}')