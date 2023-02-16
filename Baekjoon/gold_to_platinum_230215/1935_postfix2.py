# 1935_후위표기식2_postfix2

n = int(input())

sentence = str(input())

nli = [float(input()) for _ in range(n)]
# print(nli)
# print(ord('A'))
# print(ord('Z'))
stack = []

for v in sentence:
    if 'A' <= v <= 'Z':
        stack.append(nli[ord(v)-65])
    else:
        a = stack.pop()
        b = stack.pop()

        if v == '+':
            stack.append(b+a)
        elif v == '-':
            stack.append(b-a)
        elif v == '*':
            stack.append(b*a)
        elif v == '/':
            stack.append(b/a)

# ans = round(stack[0], 3)  이렇게 표기하면 2자리까지 나오지 않음 6.2, 3
ans = stack[0]
# print('{}'.format(ans, ".3f"))
print('%0.2f'%ans)