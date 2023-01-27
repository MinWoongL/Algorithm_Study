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
                if len(w_stack) != 0:
                    if w_stack[-1] == '(':
                        w_stack.pop()
                    else:
                        ans = False
                        break
                else:
                    ans = False
                    break
            elif s[i] == ']':
                if len(w_stack) != 0:
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
        if ans and not w_stack:
            print('yes')
        else:
            print('no')






