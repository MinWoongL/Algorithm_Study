# 4949_균형잡힌 세상_Balanced World

stop = True
while stop:
    w_stack = []
    ans = True
    s = input()
    if s == '.':
        stop = False
    else:
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[':
                w_stack.append(s[i])
            elif s[i] == ')':
                if len(w_stack) != 0:  # if not w_stack and w_stack[-1] == '(' 로 한 줄로 바꿀 수 있음
                    if w_stack[-1] == '(':
                        w_stack.pop()
                    else:
                        ans = False
                        break
                else:
                    ans = False
                    break
            elif s[i] == ']':
                if len(w_stack) != 0:  # 위와 같은 방법으로 한 줄로 줄이기 가능
                    if w_stack[-1] == '[':
                        w_stack.pop()
                    else:
                        ans = False
                        break
                else:
                    ans = False
                    break
            else:
                pass
        if ans and not w_stack:  # and not w_stack 조건을 추가하지 않으면 오답 -> 왜?? 전부 공백은 오답처리해야하나?
            print('yes')
        else:
            print('no')






