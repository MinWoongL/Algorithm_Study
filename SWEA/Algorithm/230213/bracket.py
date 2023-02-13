# 괄호검사
T = int(input())

for tc in range(1, T+1):
    sentence = str(input())
    stack = []

    ans = 1
    for v in sentence:
        if v == '(' or v == '{':
            stack.append(v)
        elif v == '}':
            if stack:
                c = stack.pop()
                if c != '{':
                    ans = 0
            else:
                ans = 0
                break
        elif v == ')':
            if stack:
                c = stack.pop()
                if c != '(':
                    ans = 0
            else:
                ans = 0
                break
        else:
            continue

    if stack:
        ans = 0

    print(f'#{tc} {ans}')