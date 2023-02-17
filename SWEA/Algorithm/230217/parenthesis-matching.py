# 1218_괄호짝짓기_parenthesis-matching

for tc in range(1, 11):
    N = int(input())
    parenthesis = list(map(str, input()))

    p_dict = {'(': ')', '[': ']', '<': '>', '{': '}'}

    stack = []
    ans = 1
    for c in parenthesis:
        if not stack:
            stack.append(c)
        else:
            if c in p_dict.keys():
                stack.append(c)
            else:
                if stack:
                    check = stack.pop()
                    if p_dict[check] != c:
                        ans = 0
                        break
                else:
                    ans = 0
                    break

    if stack:
        ans = 0

    print(f'#{tc} {ans}')
