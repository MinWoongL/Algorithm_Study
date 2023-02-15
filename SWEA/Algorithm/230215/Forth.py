# Forth_서울2반_이민웅

T = int(input())

for tc in range(1, T+1):
    oper_li = list(map(str, input().split()))
    stack = []
    op = ['+','-','*','/']
    for i in range(len(oper_li)):
        if oper_li[i] == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack[0]}')
                stack.clear()
                break
            else:
                print(f'#{tc} error')
                stack.clear()
        elif oper_li[i].isdigit():
            stack.append(int(oper_li[i]))
        else:
            if len(stack) > 1 and type(stack[-1]) == int:
                a = stack.pop()
                b = stack.pop()
                if oper_li[i] == op[0]:
                    stack.append(b+a)
                elif oper_li[i] == op[1]:
                    stack.append(b-a)
                elif oper_li[i] == op[2]:
                    stack.append(b*a)
                else:
                    if a == 0:
                        print(f'#{tc} error')
                    else:
                        stack.append(b//a)
            else:
                print(f'#{tc} error')
                stack.clear()
                break
    if stack:
        print(f'#{tc} error')

    # stack2 = [0]*len(oper_li)
    # top = -1
    # postfix = ''
    # op2 = {'+':1,'-':1,'*':2,'/':2}
    #
    # for t in oper_li:
    #     if '0'<=t<='9':
    #         postfix += t
    #     elif t in op2:
    #         if top==-1 or op2[stack2[top]] < op2[t]:
    #             top += 1
    #             stack2[top] = t
    #         else:
    #             while top > -1 and op2[stack2[top]] >= op2[t]:
    #                 top -= 1
    #                 postfix += stack2[top + 1]
    #             top += 1
    #             stack2[top] = t
    # while top > -1:
    #     top -= 1
    #     postfix += stack2[top+1]
    #
    # print(postfix)

