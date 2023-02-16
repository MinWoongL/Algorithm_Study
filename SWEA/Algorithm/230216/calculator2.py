# 계산기2_서울2반_이민웅

op = {'+':1, '-':1, '*':2, '/':2}

def pfix(li):
    stack = [0]*len(li)
    top = -1
    p_fix = ''

    for t in li:
        if '0' <= t <= '9':
            p_fix += t
        elif t in op:
            if top == -1 or op[stack[top]] < op[t]:
                top += 1
                stack[top] = t
            else:
                while top > -1 and op[stack[top]] >= op[t]:
                    top -= 1
                    p_fix += stack[top + 1]
                top += 1
                stack[top] = t
    while top > -1:
        top -= 1
        p_fix += stack[top + 1]
    return p_fix


def postfix_eval(text):
    stack = []
    o_li = list(map(str, text))
    for i in range(len(o_li)):
        if o_li[i].isdigit():
            stack.append(int(o_li[i]))
        else:
            if len(stack) > 1 and type(stack[-1]) == int:
                a = stack.pop()
                b = stack.pop()
                if o_li[i] == '+':
                    stack.append(b+a)
                elif o_li[i] == '-':
                    stack.append(b-a)
                elif o_li[i] == '*':
                    stack.append(b*a)
                else:
                    stack.append(b//a)

    return stack


for tc in range(1, 11):
    N = int(input())
    op_li = list(map(str, input()))
    stack = []

    post = pfix(op_li)
    result = postfix_eval(post)
    print(f'#{tc} {result[0]}')

